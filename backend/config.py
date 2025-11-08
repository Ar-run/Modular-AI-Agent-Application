import os
from dotenv import load_dotenv

load_dotenv()

#vector database config
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT")
PINECONE_INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")

# Groq config
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Tavily config
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

#Embedding model config
EMBED_MODEL = os.getenv("EMBED_MODEL", "sentence-transofrmers/all-MiniLM-L6-v2")

# Paths config (adjust as needed)
DOC_SOURCE_DIR = os.getenv("DOC_SOURCE_DIR", "data")