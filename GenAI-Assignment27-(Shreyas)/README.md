# Groq API & FastAPI Chatbot

This project focuses on building an AI chatbot using the Groq API and integrating it with FastAPI. It covers basic chatbot development, handling system and user messages, and testing multiple queries.

The project also explores Retrieval-Augmented Generation (RAG) by retrieving relevant document chunks from a vector store and generating context-based responses using Groq LLM.

A FastAPI backend is developed with `/health` and `/chat` endpoints, along with Pydantic validation, error handling, environment variable management, and logging.

Finally, the application is tested locally using Uvicorn, Postman, and Swagger UI to evaluate response latency, answer accuracy, API stability, and the benefits of an API-first GenAI architecture.