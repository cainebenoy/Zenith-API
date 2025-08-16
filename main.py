import random
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from typing import Dict, List

app = FastAPI()

# Add this CORS configuration
origins = [
    "http://localhost",
    "http://127.0.0.1",
    "file://",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Data for the quotes, stored as a list of dictionaries
QUOTES: List[Dict[str, str]] = [
    {"text": "The only way to do great work is to love what you do.", "author": "Steve Jobs"},
    {"text": "Believe you can and you're halfway there.", "author": "Theodore Roosevelt"},
    {"text": "The future belongs to those who believe in the beauty of their dreams.", "author": "Eleanor Roosevelt"},
    {"text": "It is our choices, Harry, that show what we truly are, far more than our abilities.", "author": "J.K. Rowling"},
    {"text": "The best way to predict the future is to create it.", "author": "Peter Drucker"},
    {"text": "Start where you are. Use what you have. Do what you can.", "author": "Arthur Ashe"},
    {"text": "Strive not to be a success, but rather to be of value.", "author": "Albert Einstein"}
]

@app.get("/quote")
def get_random_quote():
    """
    Returns a random inspirational quote.
    """
    random_quote = random.choice(QUOTES)
    return random_quote