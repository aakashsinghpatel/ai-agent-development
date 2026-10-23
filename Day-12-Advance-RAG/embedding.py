from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

def create_embedding(text):
    """ Method to create embedding of text """
    response = client.embeddings.create(model=os.getenv("EMBEDDING_MODEL"), input=text)
    return response.data[0].embedding

def embed_chunks(chunks):
    """ Method to create embed chunks """
    embedded_chunks = []
    for chunk in chunks:
        chunk_embedding = create_embedding(chunk["text"])
        embedded_chunks.append({**chunk, "embedding": chunk_embedding})
        """   embedded_chunks.append({
            "text": chunk["text"],
            "source": chunk["source"],
            "chunk_id": chunk["chunk_id"],
            "embedding": embedding
        }) """

    return embedded_chunks
