import random
from fastapi import FastAPI
from typing import Dict, List

app = FastAPI()

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