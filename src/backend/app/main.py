import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv  # Import the load_dotenv function
from app.controllers import process_text_controller
from app.models.db import connect_db, disconnect_db

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this to your specific origin(s)
    allow_credentials=True,
    allow_methods=["*"],  # You can specify allowed methods
    allow_headers=["*"],  # You can specify allowed headers
)

# Connect to the database when the app starts
@app.on_event("startup")
async def startup():
    await connect_db()
    print

# Disconnect from the database when the app stops
@app.on_event("shutdown")
async def shutdown():
    await disconnect_db()

# Include the router from your controller
app.include_router(process_text_controller.router)
