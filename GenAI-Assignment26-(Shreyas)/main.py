## Part 3- Building API using Fast API to Part 5- Mini Project Validation
from fastapi import FastAPI,HTTPException
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from pydantic import BaseModel,Field
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

load_dotenv()
app = FastAPI()

class ChatRequest(BaseModel):
    query : str= Field(min_length=1)


LLM = ChatGroq(model='openai/gpt-oss-20b')


@app.get("/health")
def health():
    logger.info("Health check requested")
    return {"status": "healthy"}

@app.post("/chat")
def chat(request: ChatRequest):
    logger.info("Chat request received")
    query = request.query.strip()
    # answer = 'model response'
    if not query:
        raise HTTPException(
            status_code=422,
            detail='Query Not Found'
        )
    try:
        answer = LLM.invoke(query)
        logger.info("Chat response generated successfully")
        return {"answer": answer.content}
    except Exception:
        logger.exception("Groq model request failed")
        raise HTTPException(
            status_code=502,
            detail='Groq Model Request Failed'
        )