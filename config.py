import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Fetch the API key from the environment
TOGETHER_API_KEY = os.getenv("TOGETHER_API_KEY")

# Shark Tank Configuration
MIN_VALUATION = 1000
MAX_VALUATION = 100000000
MIN_EQUITY = 1
MAX_EQUITY = 100

# Ensure the API key is loaded
if not TOGETHER_API_KEY:
    raise ValueError("TOGETHER_API_KEY is not set in the environment variables.")