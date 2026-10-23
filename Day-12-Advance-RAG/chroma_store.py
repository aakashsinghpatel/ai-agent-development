from chromadb import PersistentClient 
from pathlib import Path

chromaclient = PersistentClient(path='./chroma.db')

collection = chromaclient.get_or_create_collection(name="documents")


def add_chunks(embedded_chunks):
    """ Method to add chunks into chroma DB 
     Upsert:
     as because of this if id's already exist then also update for the smae"""
    documents = []
    embedings = []
    ids = []
    metadata = []

    for chunk in embedded_chunks:
        documents.append(chunk['text'])
        embedings.append(chunk['embedding'])
        ids.append( f'{chunk["source"]}_'f'{chunk["chunk_id"]}')
        metadata.append({
            "source": chunk['source'],
            "chunk_id": chunk['chunk_id']
        })

    collection.upsert(ids=ids, documents=documents, embeddings=embedings, metadatas=metadata)


def search_chunk(querry_embedding, top_k = 5):
    """ Method to return top_k candidates from chromaDB based on query embedding """
    return collection.query(query_embeddings=[querry_embedding], n_results=top_k)