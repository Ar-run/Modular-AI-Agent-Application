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
embeddings=HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

INDEX_NAME="rag-index"

#reteriver function to get relevant documents from pinecone vector store
def get_retriever():
  """Initialise and returns the Pinecone vector store retriever."""
  # ensure index exists otherwise create it

  if INDEX_NAME not in pc.list_indexes().names():
    print("Cresting new index")
    pc.create_index(
      name=INDEX_NAME,
      dimension = 384,
      metric = "cosine",
      spec=ServerlessSpec(cloud='aws',region='us-east-1')
    )
    print("Created Pinecone index")
  
  vectorstore=PineconeVectorStore(
    index_name=INDEX_NAME,
    embedding=embeddings
  )
  return vectorstore.as_retriever()




# uploader function to add documents to pinecone vector store
def add_document(text_content:str):
  """
  Add a single text document to the Pinecone vector store.
  Splits the text into chunks before embedding and upserting.
  """

  if not text_content:
    raise ValueError("Document content cannot be empty!")
  
  # Split the document into chunks
  text_splitter=RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=200,
    add_start_index=True
  )

  # create langchain document objects from the raw text
  documents=text_splitter.create_documents([text_content])
  print("Splitting document into chunks for indexing")

  #get vectorstore instance to add documents
  vectorstore = PineconeVectorStore(index_name=INDEX_NAME, embedding=embeddings)

  # add documents to vector store
  vectorstore.add_documents(documents)

  print(f"Successfully added {len(documents)} chunks to Pinecone vector index '{INDEX_NAME}'.")

