import random
from fastapi import FastAPI
from typing import Dict, List
app=FastAPI()
QUOTES: List[Dict[str,str]]=[
    {"text":"The only way to do great work is to love what you do.","author":"Steve Jobs"},
    