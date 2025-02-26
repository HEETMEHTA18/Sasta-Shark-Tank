import os
from dotenv import load_dotenv

load_dotenv()  # Loads variables from .env

TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Shark Tank Configuration
MIN_VALUATION = 1000
MAX_VALUATION = 100000000
MIN_EQUITY = 1
MAX_EQUITY = 100 