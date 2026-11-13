
import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_astradb import AstraDBVectorStore
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

load_dotenv()

# Load PDF
pdf_path = "demo.pdf"

loader = PyPDFLoader(pdf_path)
documents = loader.load()

print("PDF Loaded Successfully!")

# Split text into chunks
text_splitter = CharacterTextSplitter(
    separator="\n",
    chunk_size=800,
    chunk_overlap=200,
    length_function=len
)

texts = text_splitter.split_documents(documents)

print(f"Total Chunks: {len(texts)}")

# Initialize Embedding Model
embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Connect to AstraDB
astra_vector_store = AstraDBVectorStore(
    embedding=embedding_model,
    collection_name="pdf_rag_collection",
    token=os.getenv("ASTRA_DB_APPLICATION_TOKEN"),
    api_endpoint=os.getenv("ASTRA_DB_API_ENDPOINT")
)

# Store embeddings in AstraDB
astra_vector_store.add_documents(texts)

print("Documents stored in AstraDB successfully!")

# Create Retriever
retriever = astra_vector_store.as_retriever(
    search_kwargs={"k": 4}
)

# Initialize Groq LLM
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0
)

# Create Prompt Template
prompt = ChatPromptTemplate.from_template("""
You are a helpful PDF question-answering assistant.

Answer the question using ONLY the provided context.
If the answer is not available in the context,
clearly say that the information is not present in the PDF.

Context:
{context}

Question:
{question}

Answer:
""")

# RAG Chain
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


first_question = True

while True:

    if first_question:
        query_text = input(
            "Enter your Question (Or type quit to exit): "
        ).strip()
        first_question = False

    else:
        query_text = input(
            "What's your Next Question or type quit to Exit: "
        ).strip()

    if query_text.lower() in ["quit", "exit"]:
        print("Thank you for using PDF RAG!")
        break

    if not query_text:
        continue

    # Retrieve relevant chunks
    relevant_docs = retriever.invoke(query_text)

    if not relevant_docs:
        print("No relevant information found in the PDF.")
        continue

    # Prepare context
    context = format_docs(relevant_docs)

    # Generate answer
    formatted_prompt = prompt.invoke({
        "context": context,
        "question": query_text
    })

    response = llm.invoke(formatted_prompt)

    print("\nAnswer:")
    print(response.content)

    # Display source pages
    print("\nSource Pages:")
    for doc in relevant_docs:
        print(doc.metadata.get("page", "Unknown") + 1
              if isinstance(doc.metadata.get("page"), int)
              else doc.metadata.get("page", "Unknown"))

    print("-" * 60)
