import os
from fastapi import FastAPI
from dotenv import load_dotenv  # Import the load_dotenv function
from app.controllers import process_text_controller

# Load environment variables from .env file
load_dotenv()

app = FastAPI()

# Include the router from your controller
app.include_router(process_text_controller.router)
