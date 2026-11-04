# GenAI Assignment A28: Conversational RAG Chatbot with Message History

## Overview
This assignment focuses on building a conversational RAG chatbot using LangChain. It covers document retrieval, prompt engineering, conversation history management, message trimming, and multi-turn question answering.

## Tasks Completed

### Task 1: Document Ingestion & Processing
- Loaded documents using LangChain document loaders.
- Used `RecursiveCharacterTextSplitter` to split documents into smaller chunks.
- Configured chunk size and chunk overlap.

### Task 2: Embeddings & Vector Store
- Generated embeddings for document chunks.
- Stored embeddings in a vector store.
- Created a retriever to fetch relevant document context.

### Task 3: Prompt with Message History
- Created a `ChatPromptTemplate`.
- Used `MessagesPlaceholder` to include conversation history.
- Designed prompts to answer only from retrieved context.
- Instructed the model to respond with "I don't know" when information is unavailable.

### Task 4: Q&A RAG Chain with Message History
- Built a RAG chain using `RunnableParallel`.
- Integrated the retriever, prompt, LLM, and `StrOutputParser`.
- Used `RunnableWithMessageHistory` to maintain conversation history.
- Used `ChatMessageHistory` to store messages based on session IDs.

### Task 5: Chat History Management
- Implemented message storage using `SystemMessage`, `HumanMessage`, and `AIMessage`.
- Used `trim_messages` for token-based history management.
- Explored `max_tokens`, `token_counter`, `include_system`, `allow_partial`, and `start_on`.
- Understood the trade-offs between long conversation history and performance.

### Task 6: Multi-Turn Q&A Testing & Chatbot
- Tested initial factual questions.
- Tested follow-up questions referencing previous answers.
- Tested clarification questions.
- Verified conversation context preservation and document-grounded answers.
- Integrated the chatbot with Streamlit.
- Used `st.session_state` to maintain chat history across Streamlit reruns.

## Tech Stack
- Python
- LangChain
- Groq (LLM)
- Streamlit
- Vector Store
- Embeddings
- ChatMessageHistory
- RunnableWithMessageHistory
- RecursiveCharacterTextSplitter
- python-dotenv

## Learning Outcomes
- Understanding document ingestion and retrieval in RAG.
- Working with LangChain message types and prompt templates.
- Maintaining stateful conversations using message history.
- Managing token usage through chat history trimming.
- Building conversational RAG applications with Streamlit.
- Understanding multi-turn question answering and context preservation.