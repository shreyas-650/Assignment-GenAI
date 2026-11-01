from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch,RunnableLambda,RunnableParallel
from pydantic import BaseModel,Field
from typing import Literal
from langchain_community.document_loaders import TextLoader
from langchain_ollama import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_text_splitters import RecursiveCharacterTextSplitter
from dotenv import load_dotenv

load_dotenv()

docs = TextLoader('./obama.md',encoding='utf-8').load()
splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=20)
chunks = splitter.split_documents(docs)
embedding = OllamaEmbeddings(model='nomic-embed-text')
vector_store = FAISS.from_documents(chunks,embedding)
retrieval = vector_store.as_retriever(search_kwargs={'k':3})
parser_s = StrOutputParser()

# Facutal Detection
class Data(BaseModel):
    question: Literal['factual','notfactual'] = Field(description='Categorize it in factual or notfactual')

LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser_f = PydanticOutputParser(pydantic_object=Data)
prompt_f = PromptTemplate(template='Check the {query} weather it is factual or not factual and provide in this {format}',
                        input_variables=['query'],
                        partial_variables={'format':parser_f.get_format_instructions()})
query = input('Enter The Query:')


chain_f = prompt_f | LLM | parser_f
#Retrieval Response
retrieval_prompt = PromptTemplate(
    template='''
    Answer the question using the given context only.
    If the answer is not available in the context, say "Information not found".

    Context: {context}

    Question: {query}
    ''',
    input_variables=['context', 'query']
)
def format_docs(docs):
    return '\n\n'.join(doc.page_content for doc in docs)
retrieval_chain = (
    RunnableLambda(lambda x: {
        'context': format_docs(retrieval.invoke(x['query'])),
        'query': x['query']
    })
    | retrieval_prompt
    | LLM
    | parser_s
)
#LLM Response
prompt = PromptTemplate(template='Prove me response {query}',
                        input_variables=['query'])

conditional_chain = RunnableBranch(
                                (lambda x: x['classification'].question == 'factual', retrieval_chain),
    (lambda x: x['classification'].question == 'notfactual', prompt | LLM | parser_s),
    RunnableLambda(lambda x: 'Could Not Extract Details Error')
                                )

parallel_chain = RunnableParallel({
    'query': RunnableLambda(lambda x: x),
    'classification': chain_f
})

final_chain = parallel_chain | conditional_chain

response = final_chain.invoke(query)
print(response)


