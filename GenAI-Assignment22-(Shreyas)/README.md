# Assignment 22: Embedding Models and Vector Stores and Similarity Search (LangChain)

This tasks explores text embeddings, semantic similarity search, and vector databases using LangChain. It compares embedding backends and demonstrates how document chunks can be converted into vectors, stored, and retrieved with natural-language queries.

## Overview

- Generate embeddings with OpenAI, Hugging Face, and Ollama.
- Inspect embedding dimensions and sample vector values.
- Split documents into smaller chunks for embedding and retrieval.
- Perform semantic similarity search with LangChain.
- Store and retrieve vectors using FAISS and ChromaDB.
- Persist vector indexes/databases and reload them.
- Build a retrieval pipeline with interchangeable embedding models and vector stores.

## Technologies Used

- Python and LangChain
- OpenAI Embeddings
- Hugging Face Sentence Transformers: `sentence-transformers/all-MiniLM-L6-v2`
- Ollama Embeddings: `nomic-embed-text`
- FAISS
- ChromaDB
- `RecursiveCharacterTextSplitter`

## Embedding Models

### OpenAI

Uses an OpenAI embedding model, such as `text-embedding-3-small`, to convert document chunks into numerical vectors. The workflow inspects vector dimensions and sample values. An OpenAI API key is required, and API usage may incur charges.

### Hugging Face

Uses `sentence-transformers/all-MiniLM-L6-v2` to create embeddings locally. This model produces 384-dimensional vectors by default and is a lightweight option for semantic search.

### Ollama

Uses the locally running `nomic-embed-text` model to generate embeddings without sending text to a hosted embedding API. The model must be downloaded and Ollama must be running.

## Document Processing and Similarity Search

Documents are loaded and split into smaller chunks before embedding. The vectors are used to find chunks that are semantically similar to a query. LangChain's vector-store interface provides a convenient way to retrieve the top matching documents.

```text
Documents → Text Splitting → Embeddings → Vector Store → Similarity Search
```

## Vector Stores

### FAISS

FAISS provides efficient similarity search over embedding vectors. The workflow includes storing vectors, searching for relevant documents, saving an index locally, and reloading it to verify that search works.

### ChromaDB

ChromaDB stores document chunks alongside embeddings and metadata. Collections can be persisted to disk and queried later using semantic similarity search.

## Configurable Retrieval Pipeline

The pipeline combines document processing, embedding generation, vector storage, and retrieval. The embedding backend can be selected from OpenAI, Hugging Face, or Ollama, and the vector store can be selected from FAISS or ChromaDB.

## Key Learnings

- Embeddings represent text as numerical vectors that capture semantic information.
- Similarity search retrieves content based on vector similarity rather than exact keyword matches alone.
- Chunking helps process long documents and retrieve relevant passages.
- Vector stores organize embeddings and support efficient retrieval.
- FAISS is useful for local vector search, while ChromaDB provides collection-based storage and persistence.
- RAG systems can retrieve relevant context before passing it to a language model.

## Setup

Create and activate your Python environment, then install the packages for the components you plan to use:

```bash
pip install -r requirements.txt
```

Some integrations are optional; install only those needed for your selected embedding provider and vector store.

For OpenAI embeddings, create a `.env` file:

```env
OPENAI_API_KEY=your_openai_api_key
```

Keep `.env` out of version control. Never commit API keys or other secrets to GitHub.

For Ollama embeddings, install Ollama and download the model:

```bash
ollama pull nomic-embed-text
```

Make sure Ollama is running before using the model.

## Running the Project

1. Activate your Python environment.
2. Install the required dependencies.
3. Configure the OpenAI API key if using OpenAI embeddings.
4. Download `nomic-embed-text` and start Ollama if using Ollama embeddings.
5. Run the relevant notebook or Python script.
6. Load and split documents, generate embeddings, create a vector store, and test queries.

## Notes

- Use the same embedding model for indexing documents and embedding search queries.
- Embedding dimensions vary by model.
- FAISS GPU support depends on the operating system, CUDA setup, and available package builds; `faiss-cpu` is a practical option for many local projects.
- Results depend on the document chunks, embedding model, vector-store configuration, and query.
