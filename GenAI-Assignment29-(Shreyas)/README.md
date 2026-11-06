# 🤖 Multi-Model Q&A ChatBot (Cloud + Local) with LangSmith Tracing

An interactive conversational AI web application built with **Streamlit**, **LangChain (LCEL)**, **Groq**, and **Ollama**. It features dynamic model routing between cloud and local inference, multi-turn conversational memory, and end-to-end LLMOps observability via **LangSmith**.

---

## 📸 Screenshots & Observability

### 1. Streamlit Interactive Web Interface
![Streamlit Web App](web.png)

### 2. LangSmith Observability & Tracing Dashboard
![LangSmith Dashboard](langsmith.png)

---

## 🌟 Key Features

- **Hybrid Inference Architecture**:
  - **Cloud LLM**: Ultra-fast cloud inference via **Groq** (`openai/gpt-oss-20b`).
  - **Local LLM**: Privacy-focused, offline-capable local inference via **Ollama** (`llama3.2`).
- **Session-Based Conversation Memory**: Built using LangChain's `RunnableWithMessageHistory` and `ChatMessageHistory` managed via Streamlit's `session_state`.
- **Full LLMOps Observability**: Native integration with **LangSmith** for tracing, latency monitoring, token consumption, and debugging prompt pipelines.
- **Interactive UI**: Simple, clean web interface powered by **Streamlit**.

---

## 🏗️ Architecture & Workflow

```mermaid
flowchart LR
    A[User Input] --> B[Streamlit UI]
    B --> C[LangChain LCEL Chain]
    C --> D{Model Switch}
    D -->|Cloud| E[Groq API]
    D -->|Local| F[Ollama Local Engine]
    C <--> G[Session Memory / ChatMessageHistory]
    C -. Tracing .-> H[LangSmith Dashboard]
    E --> I[Output Parser]
    F --> I
    I --> B
```

---

## 📁 Project Structure

```text
├── app.py              # Main Streamlit application and LangChain logic
├── web.png             # UI screenshot of Streamlit interface
├── langsmith.png       # Screenshot of LangSmith traces dashboard
├── .env                # API keys and environment configurations (git-ignored)
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
```

---

## 📋 Prerequisites

Before running the project, ensure you have:

1. **Python 3.10+** installed.
2. A **Groq API Key** ([console.groq.com](https://console.groq.com/)).
3. A **LangSmith API Key** ([smith.langchain.com](https://smith.langchain.com/)).
4. **Ollama** installed and running locally ([ollama.com](https://ollama.com/)):
   ```bash
   ollama run llama3.2
   ```

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and Activate a Virtual Environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables
Create a `.env` file in the root directory:

```env
# Groq API
GROQ_API_KEY=gsk_your_groq_api_key_here

# LangSmith Observability
LANGCHAIN_TRACING_V2=true
LANGCHAIN_API_KEY=lsv2_pt_your_langsmith_api_key_here
LANGCHAIN_PROJECT=Streamlit-MultiModel-Chatbot
LANGCHAIN_ENDPOINT=https://api.smith.langchain.com
```

---

## 🚀 Running the Application

1. Make sure your local Ollama daemon is running:
   ```bash
   ollama serve
   ```
2. Start the Streamlit app:
   ```bash
   streamlit run app.py
   ```
3. Open your browser and navigate to `http://localhost:8501`.

---

## 📜 License

This project is licensed under the MIT License - feel free to use and modify it for your own projects!