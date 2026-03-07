from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
import os

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings

from transformers import pipeline

from rank_bm25 import BM25Okapi

app = FastAPI()

# =========================
# Global Variables
# =========================

vector_store = None
documents_store = []
chat_history = []

bm25 = None
tokenized_corpus = []

# =========================
# Embeddings
# =========================

embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# =========================
# Load Existing Vector DB
# =========================

if os.path.exists("vector_db"):
    vector_store = FAISS.load_local(
        "vector_db",
        embeddings,
        allow_dangerous_deserialization=True
    )

# =========================
# Request Schema
# =========================

class Query(BaseModel):
    question: str

# =========================
# Upload PDF
# =========================

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):

    global vector_store, documents_store, bm25, tokenized_corpus

    os.makedirs("documents", exist_ok=True)

    file_path = f"documents/{file.filename}"

    with open(file_path, "wb") as f:
        f.write(await file.read())

    loader = PyPDFLoader(file_path)
    documents = loader.load()

    for doc in documents:
        doc.metadata["source"] = file.filename

    documents_store.extend(documents)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    chunks = splitter.split_documents(documents)

    # =========================
    # Vector Store
    # =========================

    if vector_store is None:
        vector_store = FAISS.from_documents(chunks, embeddings)
    else:
        vector_store.add_documents(chunks)

    vector_store.save_local("vector_db")

    # =========================
    # BM25 Index
    # =========================

    texts = [doc.page_content for doc in chunks]

    tokenized_corpus = [text.split() for text in texts]

    bm25 = BM25Okapi(tokenized_corpus)

    return {
        "message": f"{file.filename} uploaded successfully"
    }

# =========================
# Ask Question
# =========================

@app.post("/ask")
def ask_question(query: Query):

    global vector_store, chat_history, bm25

    if vector_store is None:
        return {"answer": "Please upload a document first."}

    try:

        # =========================
        # Vector Search
        # =========================

        vector_docs = vector_store.similarity_search(query.question, k=3)

        # =========================
        # BM25 Search
        # =========================

        tokenized_query = query.question.split()

        bm25_scores = bm25.get_scores(tokenized_query)

        top_bm25_indices = sorted(
            range(len(bm25_scores)),
            key=lambda i: bm25_scores[i],
            reverse=True
        )[:3]

        bm25_docs = [
            documents_store[i]
            for i in top_bm25_indices
            if i < len(documents_store)
        ]

        # =========================
        # Combine Results
        # =========================

        docs = vector_docs + bm25_docs

        context = "\n".join([doc.page_content for doc in docs])

        sources = list(set(
            doc.metadata.get("source", "unknown")
            for doc in docs
        ))

        prompt = f"""
You are an AI research assistant.

Conversation History:
{chat_history}

Context:
{context}

Question:
{query.question}

Provide a clear answer.
"""

        generator = pipeline(
            "text2text-generation",
            model="google/flan-t5-base",
            max_new_tokens=200
        )

        result = generator(prompt)

        answer = result[0]["generated_text"]

        chat_history.append({
            "question": query.question,
            "answer": answer
        })

        return {
            "answer": answer,
            "sources": sources
        }

    except Exception as e:

        return {
            "error": str(e)
        }