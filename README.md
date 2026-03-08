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

# Installation

### 1 Clone the repository

```
git clone https://github.com/yourusername/ai-research-assistant.git
```

```
cd ai-research-assistant
```

---

### 2 Create a virtual environment

```
python -m venv venv
```

Activate the environment.

Windows

```
venv\Scripts\activate
```

Mac / Linux

```
source venv/bin/activate
```

---

### 3 Install dependencies

```
pip install -r requirements.txt
```

---

# Running the Project Locally

The project consists of two components:

- Backend API (FastAPI)
- Frontend Interface (Streamlit)

Both services must be running.

---

## Step 1 Start Backend Server

Run the FastAPI backend.

```
uvicorn api.rag_api:app --reload
```

Backend will start at:

```
http://127.0.0.1:8000
```

API documentation is available at:

```
http://127.0.0.1:8000/docs
```

---

## Step 2 Start Frontend

Open another terminal and run:

```
streamlit run ui/app.py
```

The Streamlit interface will start at:

```
http://localhost:8501
```

Open the URL in your browser.

---

# Using the Assistant

1 Upload a research paper  
2 Wait for the system to index the document  
3 Ask questions related to the paper  
4 The assistant retrieves relevant context and generates an answer  

The response is grounded in retrieved document passages, improving factual accuracy.

---

# Example Queries

Example questions you can ask:

- What dataset was used in this paper?
- What methodology does the author propose?
- What are the key contributions of the paper?
- What evaluation metrics were used?
- What are the limitations of the proposed method?

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
