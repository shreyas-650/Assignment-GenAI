from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel,Field
from typing import Literal,Optional
from langchain_core.output_parsers import PydanticOutputParser

load_dotenv()

class Answer(BaseModel):
    answer: str = Field(description='It contains answer')
    confidence: float = Field(gt=0,lt=5,description='Contains Confidence Rating')
    source: str = Field(description='Contain source details')

model = ChatGoogleGenerativeAI(model='gemini-2.5-flash')
parser = PydanticOutputParser(pydantic_object=Answer)
prompt = PromptTemplate(template='Give me answer of this question {query} in 20 words and it condifence and source in this {format}',
                        input_variables=['query'],
                        partial_variables={'format': parser.get_format_instructions()})

chain = prompt | model | parser

response = chain.invoke({'query':'Who is SRK?'})
print(response)
