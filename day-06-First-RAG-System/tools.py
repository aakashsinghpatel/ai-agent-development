
from pathlib import Path
import numpy as np

def load_documents():
    """ Tool to load  knowledgebase (all documents) and return dictionaty of doc {filename: content} """
    documents = {}
    folder = Path('knowledge')
    for file in folder.glob('*.txt'):
        documents[file.name] = file.read_text(encoding='utf-8')

    return documents

def create_embedding(client, content):
    """ Tool to create embedding of passed content """
    embedding_res = client.embeddings.create(model='nomic-embed-text', 
                                              input=content)
    return embedding_res.data[0].embedding

def cosine_similarity(embedding1, embedding2):
    """ Tool to find cosine similarity score between two embedding """
    vector1 = np.array(embedding1)
    vector2 = np.array(embedding2)
    dot_product = np.dot(vector1, vector2)
    norm_a = np.linalg.norm(vector1)
    norm_b = np.linalg.norm(vector2)

    # Compute cosine similarity
    cosine_sim_score = dot_product / (norm_a * norm_b)
    return cosine_sim_score
    