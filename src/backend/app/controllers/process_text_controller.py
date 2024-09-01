from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.models.db import execute_query
from dotenv import load_dotenv
import os
import logging
import google.generativeai as genai
import re
import sqlparse

load_dotenv()

# Initialize the Gemini API key
api_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=api_key)

model = genai.GenerativeModel('gemini-pro')

router = APIRouter()

class TextRequest(BaseModel):
    text: str

def generate_sql_query(text: str) -> str:
    initial_prompt = """
    Você é um assistente especializado em gerar consultas SQL para um banco de dados PostgresSQL. O banco possui a seguinte tabela chamada 'purchases', que contém informações detalhadas sobre transações financeiras:

    CREATE TABLE purchases (
        id BIGINT PRIMARY KEY,  -- Identificador único da transação
        status VARCHAR(50),  -- Status da transação (denied, confirmed, canceled, approved, voided)
        created TIMESTAMP,  -- Data e hora em que a transação foi criada ou processada
        cardId BIGINT,  -- Identificador único do cartão utilizado na transação
        holderId BIGINT,  -- Identificador único do titular do cartão que realizou a transação
        amount DECIMAL(20, 2),  -- Valor monetário da transação
        merchantName VARCHAR(255),  -- Nome do estabelecimento ou comerciante onde a transação foi realizada
        merchantCategoryType VARCHAR(255),  -- Categoria do tipo de negócio ou serviço fornecido pelo comerciante (hotels, services, retail, clothing, airlines,
           financial, nan, carRental, food, transportation,
           education, leisure, government, organizations, health,
           gambling, groceries, fuel, pets)
        workspaceId BIGINT  -- Identificador único do workspace ou conta corporativa associada à transação
    );

    Instruções importantes:
    - Sempre que possível, minimize a consulta gerada, incluindo apenas as colunas necessárias para a resposta.
    - Ao filtrar pela coluna status ou merchantCategoryType, lembre-se de usar CAST(status AS VARCHAR) ou CAST(merchantCategoryType AS VARCHAR) se houver possibilidade de comparação com valores numéricos.
    - Ao filtrar pela coluna amount, use CAST(amount AS TEXT) ao comparar com valores de texto.
    - Considere as melhores práticas de otimização SQL para garantir que as consultas sejam eficientes e escaláveis.

    Com base nas informações que eu fornecer a partir de agora, gere apenas a query SQL para a consulta desejada, sem mais comentários. Leve em consideração que o banco de dados é usado para analisar transações financeiras, e as queries podem envolver filtros específicos, agregações ou combinações de colunas para gerar relatórios precisos:
    """
    prompt = initial_prompt + text
    response = model.generate_content(prompt)
    return response.text.strip()

def validate_sql(sql_query: str) -> bool:
    try:
        parsed = sqlparse.parse(sql_query)
        if not parsed:
            return False
        for statement in parsed:
            if statement.get_type() not in ['SELECT', 'INSERT', 'UPDATE', 'DELETE']:
                return False
        return True
    except Exception as e:
        logging.error(f"SQL validation error: {e}")
        return False

def dry_run_sql(sql_query: str) -> bool:
    try:
        result = execute_query(f"EXPLAIN {sql_query}")
        return True if result else False
    except Exception as e:
        logging.error(f"Dry-run execution failed: {e}")
        return False

def answer_question(question: str, query_result: list) -> str:
    query_data = "\n".join([str(row) for row in query_result])
    prompt = f"""
    Você é um assistente especializado em responder perguntas baseadas em dados corporativos. Vou lhe fornecer uma pergunta e os dados resultantes de uma consulta SQL. Por favor, formule uma resposta detalhada e direta usando as informações fornecidas.

    Pergunta: {question}

    Dados resultantes da consulta SQL:
    {query_data}

    Resposta detalhada:
    """
    response = model.generate_content(prompt)
    return response.text.strip()

@router.post("/process-text/")
async def process_text(request: TextRequest):
    max_iterations = 5
    attempt = 0

    while attempt < max_iterations:
        try:
            attempt += 1
            sql_query_extracted = None

            for i in range(max_iterations):
                sql_query = generate_sql_query(request.text)
                print(f"Attempt {attempt}, Iteration {i + 1}: Generated SQL Query: {sql_query}")

                matches = re.findall(r'```sql(.*?)```', sql_query, re.DOTALL)
                if matches:
                    sql_query_extracted = " ".join([match.strip() for match in matches])
                    if validate_sql(sql_query_extracted) and dry_run_sql(sql_query_extracted):
                        break
                    else:
                        logging.warning(f"Attempt {attempt}, Iteration {i + 1}: SQL is not valid or failed dry run.")
                else:
                    logging.warning(f"Attempt {attempt}, Iteration {i + 1}: No valid SQL found.")
            
            if not sql_query_extracted or i == max_iterations - 1:
                raise ValueError("Não foi possível gerar uma consulta SQL válida após várias tentativas.")

            print("Validated SQL Query:", sql_query_extracted)

            result = await execute_query(sql_query_extracted)
            print("Query result:", result)

            response_text = answer_question(request.text, result)
            return {"response": response_text}

        except Exception as e:
            logging.error(f"Attempt {attempt}: Error occurred: {e}", exc_info=True)
    
    raise HTTPException(status_code=500, detail="Não foi possível gerar e executar uma consulta SQL válida após várias tentativas.")
