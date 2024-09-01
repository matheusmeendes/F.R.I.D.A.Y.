from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.db import execute_query  # Ensure this import path is correct
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

# Initialize the Groq client with your API key
api_key = os.getenv('GROQ_API_KEY')
client = Groq(api_key=api_key)

router = APIRouter()

class TextRequest(BaseModel):
    text: str

def generate_sql_query(text: str) -> str:
    initial_prompt = """
    Você é um assistente especializado em gerar consultas SQL para um banco de dados. O banco possui a seguinte tabela:

    CREATE TABLE purchases (
        id BIGINT PRIMARY KEY,
        status VARCHAR(50),
        created TIMESTAMP,
        cardId BIGINT,
        holderId BIGINT,
        amount DECIMAL(20, 2),
        merchantName VARCHAR(255),
        merchantCategoryType VARCHAR(255),
        workspaceId BIGINT
    );

    Com base nas informações que eu fornecer a partir de agora, gere apenas a query SQL para a consulta desejada, sem mais comentários:
    """
    prompt = initial_prompt + text
    response = client.chat.completions.create(
        messages=[{
            "role": "user",
            "content": prompt
        }],
        model="llama-3.1-8b-instant"
    )
    return response.choices[0].message.content

@router.post("/process-text/")
async def process_text(request: TextRequest):
    try:
        # Generate SQL query using LLaMA
        sql_query = generate_sql_query(request.text)

        # Execute the SQL query
        result = await execute_query(sql_query)

        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
