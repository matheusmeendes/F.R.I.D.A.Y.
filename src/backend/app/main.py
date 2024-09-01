import os
from fastapi import FastAPI
from dotenv import load_dotenv
from app.controllers import process_text_controller, upload_controller
from app.models.db import connect_db, disconnect_db

# Load environment variables from .env file
load_dotenv()

# Debug: Check if the environment variables are loaded correctly
print(f"Loaded DATABASE_URL: {os.getenv('DATABASE_URL')}")
print(f"Loaded GROQ_API_KEY: {os.getenv('GROQ_API_KEY')}")

app = FastAPI()

# Connect to the database when the app starts
@app.on_event("startup")
async def startup():
    await connect_db()
    print("Database connected successfully")

# Disconnect from the database when the app stops
@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()
    print("Database disconnected successfully")

# Include the router from your controller
app.include_router(process_text_controller.router)
app.include_router(upload_controller.router)

# Debug: Start the server manually to see output
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
