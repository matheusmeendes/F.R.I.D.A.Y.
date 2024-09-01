import os
from databases import Database
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get the database URL from the environment variable
DATABASE_URL = os.getenv('DATABASE_URL')

# Initialize the database connection
database = Database(DATABASE_URL)

async def connect_db():
    await database.connect()

async def disconnect_db():
    await database.disconnect()

async def execute_query(sql_query: str):
    """
    Execute the SQL query and return the results.
    """
    try:
        result = await database.fetch_all(query=sql_query)
        return result
    except Exception as e:
        raise ValueError(f"Error executing query: {e}")
