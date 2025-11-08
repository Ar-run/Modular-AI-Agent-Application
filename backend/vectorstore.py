import os
from pinecone import Pinecone,ServerlessSpec
from langchain_pinecone import PineconeVectorStore
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import PINECONE_API_KEY

#SET ENVIRONMENT VARIABLES FOR PINECONE
os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

#intitilise pinecone client
pc=Pinecone(api_key=PINECONE_API_KEY)

#define embedding models
embedding=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

#reteriver function to get relevant documents from pinecone vector store
def get_retriever():
  pass

# uploader function to add documents to pinecone vector store
def add_document():
  pass

