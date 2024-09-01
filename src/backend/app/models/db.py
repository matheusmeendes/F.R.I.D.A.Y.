import os
import asyncpg
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the database URL from the environment variable
DATABASE_URL = os.getenv('DATABASE_URL')

# Custom function to create a connection pool with statement cache disabled
async def create_pool():
    return await asyncpg.create_pool(DATABASE_URL, statement_cache_size=0)

# Initialize the connection pool
pool = None

async def connect_db():
    global pool
    pool = await create_pool()

async def disconnect_db():
    global pool
    if pool:
        await pool.close()

async def execute_query(sql_query: str):
    """
    Execute the SQL query and return the results.
    """
    try:
        async with pool.acquire() as connection:
            result = await connection.fetch(sql_query)
        return result
    except Exception as e:
        raise ValueError(f"Error executing query: {e}")
