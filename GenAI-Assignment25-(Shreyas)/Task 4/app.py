from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from dotenv import load_dotenv

load_dotenv()

# Define Pydantic schema
class Answer(BaseModel):
    answer: str
    confidence: float
    source: str

# Initialize LLM and parser
LLM = ChatGoogleGenerativeAI(model='gemini-2.5-flash')

parser = PydanticOutputParser(pydantic_object=Answer)

# Create prompt
template = PromptTemplate(
    template="""
    Answer the following question.

    Question: {query}

    {format_instructions}
    """,
    input_variables=['query'],
    partial_variables={
        'format_instructions': parser.get_format_instructions()
    }
)

# Take user input
query = input('Enter your Query: ')

prompt = template.format(query=query)

try:
    # First attempt
    response = LLM.invoke(prompt)

    try:
        result = parser.parse(response.content)

    except Exception as e:
        print("Invalid output. Retrying...")

        # Retry with error details
        retry_prompt = f"""
        Your previous response did not follow the required schema.

        Original Question: {query}

        Previous Response: {response.content}

        Error: {str(e)}

        Correct the response and follow this format:
        {parser.get_format_instructions()}
        """

        retry_response = LLM.invoke(retry_prompt)

        # Parse retry response
        result = parser.parse(retry_response.content)

    print("\nStructured Output:")
    print(result.model_dump())

except Exception as e:
    print("Failed after retry:", e)

    # Fallback response
    result = Answer(
        answer="Unable to generate a valid response.",
        confidence=0.0,
        source="Fallback"
    )

    print("\nFallback Output:")
    print(result.model_dump())