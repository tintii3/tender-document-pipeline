import os
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# Retrieve the OpenAI API key from environment variables
API_KEY = os.getenv('OPENAI_API_KEY')

# Retrieve the database path from environment variables, defaulting to 'tender_documents.db' if not set
DATABASE_PATH = os.getenv("DATABASE_PATH", "tender_documents.db")
