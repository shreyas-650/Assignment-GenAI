import streamlit as st
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_classic.retrievers import MultiQueryRetriever
from langchain_core.runnables import RunnablePassthrough,RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_community.chat_message_histories import ChatMessageHistory
from dotenv import load_dotenv
from operator import itemgetter
import os
import tempfile
load_dotenv()

st.title('PDF RAG Assistant')
st.markdown("Upload a PDF document and ask questions about its content. Get relevant, context-based answers powered by Retrieval-Augmented Generation (RAG).")
st.sidebar.title('Upload Your PDF')
path = st.sidebar.file_uploader("Upload a PDF file", type=["pdf"])



query = st.sidebar.text_input('Enter The Query')

if 'store' not in st.session_state:
    st.session_state.store = {}

def get_history(session_id : str):
    if session_id not in st.session_state.store:
        st.session_state.store[session_id]=ChatMessageHistory()
    return st.session_state.store[session_id]

LLM = ChatGroq(model='openai/gpt-oss-20b',temperature=0.5)
prompt = ChatPromptTemplate([
    ('system','You have to answer the question from this context only, If the context is not sufficient say I do not Know, {context}'),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{query}')
])

if not path:
    st.info("Upload a PDF to start")
    st.stop()

with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(path.getbuffer())
        tmp_path = tmp.name
docs = PyPDFLoader(tmp_path).load()

os.remove(tmp_path)

splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=50)
chunks = splitter.split_documents(docs)
embedding = HuggingFaceEmbeddings(model='sentence-transformers/all-MiniLM-L6-v2')
vector_store = FAISS.from_documents(chunks,embedding)
retriever = MultiQueryRetriever.from_llm(retriever=vector_store.as_retriever(),llm=LLM)
def format_docs(docs):
    return "\n\n---\n\n".join(doc.page_content for doc in docs)

chain = (
    RunnablePassthrough.assign(
        context=itemgetter("query") | retriever | format_docs
    )| prompt | LLM | StrOutputParser()
    )

chatbot = RunnableWithMessageHistory(
    chain,
    get_history,
    input_messages_key='query',
    history_messages_key='history'

)
if st.sidebar.button('Invoke'):
    if query:
        response = chatbot.invoke({'query':query},
            config={'configurable':{'session_id':'user_1'}})

        st.write(response)
    else:
        st.warning("Please enter a query first.")

for session_id, history in st.session_state.store.items():
    st.write(f"Session: {session_id}")
    for message in history.messages:
        st.write(f"{message.type}: {message.content}")

