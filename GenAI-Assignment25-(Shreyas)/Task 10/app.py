from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_ollama import ChatOllama
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter


docs = TextLoader('./obama.md',encoding='utf-8').load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
chunks = splitter.split_documents(docs)
embedding = OllamaEmbeddings(model='nomic-embed-text')
vector_store = FAISS.from_documents(chunks,embedding)
retrieval = vector_store.as_retriever(search_kwargs={'k':3})

prompt = PromptTemplate(template='Give me very short detail from this context {query} only, do not use any other context',
                        input_variables=['query'])
LLM = ChatOllama(model='llama3.2')
parser = StrOutputParser()

#LCEL Pipeline
chain = retrieval | prompt | LLM | parser

result = chain.invoke('Obama')
print(result)
