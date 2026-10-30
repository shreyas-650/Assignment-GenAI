# Assignment 22: Embedding Models, Vector Stores and Similarity Search (LangChain)

This assignment explores text embeddings, semantic similarity search, vector databases, and Retrieval-Augmented Generation (RAG) using LangChain. It compares embedding models, builds vector stores, evaluates advanced retrieval strategies, and ends with a YouTube transcript RAG chatbot.

## Technologies Used

Python, LangChain, OpenAI API, Hugging Face Sentence Transformers, Ollama, FAISS, ChromaDB, RecursiveCharacterTextSplitter, YouTube Transcript API

## Installation Prerequisites

- Python 3.10+ and the latest pip
- OpenAI API key (embeddings, Multi-Query retrieval, chatbot; usage may incur charges)
- [Ollama](https://ollama.com) installed (for local embeddings)
- Optional: Jupyter Notebook or VS Code

Required libraries:

```
langchain, langchain-openai, langchain-community, langchain-huggingface,
langchain-ollama, langchain-text-splitters, faiss-cpu, chromadb,
sentence-transformers, youtube-transcript-api, pytube, python-dotenv
```

## Setup

```bash
git clone <your-repository-url>
cd <repository-name>
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Create a `.env` file (add it to `.gitignore`; never commit API keys):

```env
OPENAI_API_KEY=your_openai_api_key
```

Set up Ollama and keep it running while generating Ollama embeddings:

```bash
ollama pull nomic-embed-text
ollama serve
```

Then run the notebooks or scripts in order: embeddings, vector stores, retrieval strategies, YouTube RAG chatbot.

## Tasks and Outcomes

### 1. Embedding Models

- **OpenAI:** `text-embedding-3-small` (hosted API)
- **Hugging Face:** `sentence-transformers/all-MiniLM-L6-v2` (local)
- **Ollama:** `nomic-embed-text` (local)

**Outcome:** Generated embeddings for the same text with all three models and inspected their dimensions and values. Dimensions: OpenAI `[add value]`, Hugging Face `[add value]`, Ollama `[add value]`. Observation: `[Add your observation here]`

### 2. Vector Stores

- **FAISS:** create index, store embeddings, similarity search, save and reload locally.
- **ChromaDB:** create collection, store embeddings and metadata, similarity search, persist and reload.

**Outcome:** Both stores returned relevant documents for natural-language queries, and reloaded indexes `[matched / differed from]` the originals. Observation: `[Add FAISS vs ChromaDB observation here]`

### 3. Advanced Retrieval Strategies

- **MMR Retriever:** balances relevance and diversity to reduce redundant results.
- **Multi-Query Retriever:** an LLM generates multiple query variants and combines the results.
- **Contextual Compression:** keeps only the relevant parts of retrieved documents.

**Outcome:** `[Add how MMR, Multi-Query and Contextual Compression differed from baseline similarity search on your test query, and which worked best.]`

### 4. YouTube RAG Chatbot

Loaded the transcript with `YoutubeLoader`, split it into chunks, stored OpenAI embeddings in FAISS/ChromaDB, and built a conversational chain with an OpenAI chat model and conversation memory. Tested with at least five questions, including unrelated questions and information missing from the transcript.

**Outcome:** `[Add accuracy across the five questions, handling of unanswerable questions, and follow-up/context handling.]`

## RAG Architecture

```text
YouTube Video → Transcript Extraction → Text Splitting → Embedding Generation
      → Vector Store (FAISS / ChromaDB) → Retriever → Relevant Context
      → OpenAI Chat Model → Generated Answer
```

## Key Learnings

- Embedding models turn text into vectors whose dimensions depend on the model.
- OpenAI, Hugging Face, and Ollama embeddings differ in hosting, cost, and setup.
- FAISS and ChromaDB enable semantic search with different storage workflows.
- MMR, Multi-Query, and Contextual Compression address redundancy, query phrasing, and noisy context.
- RAG grounds LLM answers in retrieved context.

## Notes

- Use the same embedding model for indexing and querying.
- Retrieval quality depends on chunking, embedding model, and retriever settings.
- OpenAI usage may incur charges; Hugging Face and Ollama models run locally.

---

**Domain:** Generative AI | LangChain | RAG | Vector Databases