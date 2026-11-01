
# Assignment 25: Prompting & LangChain Chains

This assignment focuses on building LLM-powered applications using LangChain, covering prompt engineering, structured outputs, chains, conditional execution, parallel execution, and LangChain Expression Language (LCEL).

## 🎯 Objectives

- Understand Prompt Templates and Chat Prompt Templates.
- Generate structured LLM outputs using Pydantic.
- Implement validation and error handling.
- Build simple, conditional, and parallel chains.
- Understand Runnable components and LCEL.
- Build a Retrieval-Augmented Generation (RAG) pipeline.

## 🛠️ Tech Stack

- Python
- LangChain
- Gemini 2.5 Flash
- Ollama
- FAISS
- Pydantic
- Google Generative AI
- Python-dotenv

## 📚 Assignment Tasks

### Part 1: Prompt Templates

**Task 1: PromptTemplate**
- Created PromptTemplate with system instructions and user question placeholders.
- Injected user input dynamically.
- Tested with multiple inputs.

**Task 2: ChatPromptTemplate & Message Templates**
- Implemented ChatPromptTemplate.
- Used SystemMessage and HumanMessage.
- Explored AIMessage for conversation structure.
- Compared ChatPromptTemplate with PromptTemplate.

### Part 2: Structured Output Using Pydantic

**Task 3: Pydantic Output Schema**
- Defined Pydantic models for structured chatbot responses.
- Used LangChain output parsers.
- Generated structured outputs containing answer, confidence, and source.

**Task 4: Validation & Error Handling**
- Handled invalid LLM outputs.
- Explored retry and fallback mechanisms when the expected schema is not followed.

### Part 3: Chains in LangChain

**Task 5: Simple Chain**
- Created a basic Prompt → LLM → Output Parser pipeline.
- Executed the chain using LangChain Expression Language.

**Task 6: Conditional Chain**
- Built a conditional question-answering pipeline.
- Classified queries as factual or non-factual.
- Routed factual questions through document retrieval.
- Used direct LLM responses for non-factual questions.
- Implemented conditional routing using RunnableBranch.

**Task 7: Parallel Chain**
- Executed multiple chains in parallel.
- Generated answers, summaries, and follow-up questions.
- Combined the outputs into a unified response.

**Task 9: LCEL-Based RAG Chain**
- Built a Retrieval-Augmented Generation pipeline using LCEL.
- Connected Retriever, Prompt, LLM, and Output Parser.
- Tested the pipeline with multiple user queries.

## 🔄 Conditional RAG Pipeline

The conditional chain uses query classification to decide which execution path to follow.

```text
                 User Query
                      |
                      v
               RunnableParallel
                /           \
       Original Query    Query Classification
                              |
                              v
                       Gemini 2.5 Flash
                              |
                              v
                       RunnableBranch
                       /           \
                  Factual        Non-Factual
                     |                |
                     v                v
                FAISS Search     Direct LLM
                     |                |
                     v                |
               Context + Query        |
                     |                |
                     v                |
                   Gemini 2.5 Flash
                       \           /
                        \         /
                         v       v
                       Final Answer
```

### Key Components

| Component | Purpose |
|---|---|
| RunnableParallel | Runs multiple operations while preserving their outputs. |
| RunnableBranch | Selects an execution path based on a condition. |
| RunnableLambda | Converts a Python function into a runnable. |
| RunnablePassthrough | Passes input through without modification. |
| FAISS | Stores and retrieves document embeddings. |
| PydanticOutputParser | Parses LLM output into a structured Pydantic model. |
| StrOutputParser | Converts model output into a string. |

## ⚙️ Installation & Setup

### 1. Clone the repository

```bash
git clone https://github.com/shreyas-650/Assignment-GenAI/tree/main/GenAI-Assignment25-(Shreyas)
cd <repository-folder>
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows:**
```bash
venv\Scripts\activate
```

**Linux / macOS:**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project directory:

```env
GOOGLE_API_KEY=your_google_api_key
```

Keep your API keys private. Do not upload `.env` to GitHub.

### 5. Run the scripts

Navigate to the required task directory and execute:

```bash
python app.py
```

Some tasks may require Ollama to be installed and running locally.

For the embedding model:

```bash
ollama pull nomic-embed-text
```

For the language model:

```bash
ollama pull llama3.2
```

## 📂 Project Structure

```text
Assignment-GenAI/
│
└── Assignment25-(Shreyas)/
    │
    ├── Task 1/
    ├── Task 2/
    ├── Task 3/
    ├── Task 4/
    ├── Task 5/
    ├── Task 6/
    ├── Task 7/
    ├── Task 8/
    ├── Task 9/
    ├── Task 10/
    └── Task 11/

```

Each task contains its respective implementation and supporting files.

## 📖 Key Learnings

- Working with different prompt templates.
- Generating structured outputs with Pydantic.
- Building reusable LLM chains.
- Understanding LCEL and Runnable components.
- Implementing conditional and parallel execution.
- Integrating vector databases with retrieval pipelines.
- Building context-aware question-answering systems using RAG.

---

