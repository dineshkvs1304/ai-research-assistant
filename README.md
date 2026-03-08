# AI Research Assistant

A lightweight **Retrieval-Augmented Generation (RAG) based research assistant** designed to help users explore and query research papers efficiently.  
The system processes academic documents, converts them into vector embeddings, and retrieves the most relevant context to generate accurate answers using a language model.

This project demonstrates how modern **LLM-powered retrieval systems** can be used to interact with research literature in a natural and intuitive way.

---

# Overview

Reading research papers often involves navigating large documents, scanning sections, and repeatedly searching for relevant information. This project addresses that problem by creating an intelligent assistant capable of answering questions directly from uploaded research papers.

The assistant works by breaking documents into smaller chunks, embedding them into a vector database, retrieving the most relevant passages for a query, and using a language model to generate context-aware answers.

The result is an interactive interface where users can ask questions about research papers and receive concise answers grounded in the original document content.

---

# Key Features

- Upload and process research papers
- Semantic search over document content
- Retrieval-Augmented Generation pipeline
- Vector database for efficient similarity search
- Interactive Streamlit interface
- FastAPI backend for scalable API access
- Modular architecture for easy extension

---

# System Architecture

The system follows a **Retrieval-Augmented Generation (RAG)** architecture.

```
User Question
     │
     ▼
Streamlit Interface
     │
     ▼
FastAPI Backend
     │
     ▼
Retriever (Vector Search)
     │
     ▼
Relevant Document Chunks
     │
     ▼
LLM Generator
     │
     ▼
Final Answer
```

The pipeline consists of three stages:

### 1. Document Processing
The uploaded research paper is parsed and split into smaller chunks to preserve semantic meaning while ensuring efficient retrieval.

### 2. Embedding and Storage
Each chunk is converted into vector embeddings using a transformer-based embedding model and stored in a vector database.

### 3. Retrieval and Generation
When a question is asked:

1. The user query is converted into embeddings  
2. Similar document chunks are retrieved using vector similarity search  
3. Retrieved chunks are passed as context to the language model  
4. The language model generates the final answer  

---

# System Design Explanation

This system is built using a **Retrieval-Augmented Generation (RAG)** architecture, which combines information retrieval with large language models to generate more reliable responses.

Traditional LLM systems often hallucinate answers because they rely only on their training data. RAG addresses this limitation by grounding responses in external documents.

### Document Ingestion

When a research paper is uploaded:

- The PDF is parsed using a document loader.
- The text is split into smaller segments using a recursive text splitter.
- Each chunk retains contextual meaning while remaining small enough for embedding.

### Embedding Generation

Each chunk is converted into a numerical vector representation using the **sentence-transformers embedding model**:

```
sentence-transformers/all-MiniLM-L6-v2
```

These embeddings capture the semantic meaning of the text.

### Vector Storage

The embeddings are stored in a **FAISS vector database**, which enables fast similarity search across thousands of document chunks.

### Query Processing

When a user submits a question:

1. The query is embedded into a vector
2. The vector database retrieves the most relevant document chunks
3. These chunks become the **context** for the language model

### Answer Generation

The retrieved context is passed into a language model (HuggingFace Transformers pipeline).  
The model generates an answer using both the retrieved context and the user question.

This design significantly improves answer accuracy while reducing hallucinations.

---

# Project Structure

```
ai-research-assistant
│
├── api
│   └── rag_api.py
│
├── src
│   ├── embeddings
│   │   └── embedder.py
│   │
│   ├── ingestion
│   │   └── document_loader.py
│   │
│   ├── retrieval
│   │   └── retriever.py
│   │
│   ├── llm
│   │   └── generator.py
│   │
│   └── vectorstore
│       └── vector_db.py
│
├── ui
│   └── app.py
│
├── documents
│
├── vector_db
│
├── requirements.txt
│
└── README.md
```

---

# Tech Stack

### Backend
- FastAPI
- LangChain
- FAISS Vector Database

### Frontend
- Streamlit

### Embedding Model
- Sentence Transformers

### Language Model
- HuggingFace Transformers

### Programming Language
- Python

---

# Run Locally

## 1. Clone Repository

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/ai-research-assistant.git
```

```bash
cd ai-research-assistant
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

---

## 3. Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Mac / Linux

```bash
source venv/bin/activate
```

---

## 4. Install Dependencies

```bash
pip install -r requirements.txt
```

If `requirements.txt` is not present:

```bash
pip install fastapi uvicorn streamlit langchain langchain-community sentence-transformers faiss-cpu transformers pypdf python-multipart
```
---

## 6. Start Backend

```bash
uvicorn api.rag_api:app --reload
```

Backend URL

```
http://127.0.0.1:8000
```

API Docs

```
http://127.0.0.1:8000/docs
```

---

## 7. Start Frontend

Open new terminal.

Activate environment.

```bash
venv\Scripts\activate
```

Run Streamlit.

```bash
streamlit run ui/app.py
```

Frontend URL

```
http://localhost:8501
```

---

## 8. Upload Research Paper

Upload PDF using Streamlit UI.

---

## 9. Ask Questions

Enter question in input field.

Example queries

```
What dataset was used in this paper?
What methodology does the paper propose?
What are the key contributions?
What evaluation metrics were used?
```

---

# Future Improvements

Planned improvements include:

- Multi-document support
- Citation-aware responses
- Hybrid search (semantic + keyword)
- Improved document parsing
- Cloud deployment
- Docker containerization
- Authentication system

---

# Why This Project

This project demonstrates how **large language models can be combined with vector search systems to build intelligent knowledge assistants**.

The same architecture can be extended to:

- Legal document assistants
- Medical literature assistants
- Enterprise knowledge bases
- Technical documentation search systems


---

# Author 

Kandyana Venkata Sai Dinesh.
