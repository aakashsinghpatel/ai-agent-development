import numpy as np
from embedding import create_embedding

def cosine_similarity(embedding1, embedding2):
    """ Gives cosine similarity score between two embeddings """
    v1 = np.array(embedding1)
    v2 = np.array(embedding2)
    return np.dot(v1, v2) / (
            np.linalg.norm(v1) *
            np.linalg.norm(v2)
        )

def  sementic_search(query, chunks, top_k):
    """ It will give top_k candidate from chunks realted to query based on sementic search"""
    query_embedding = create_embedding(query)
    result = []
    for chunk in chunks:
        score = cosine_similarity(query_embedding, chunk['embedding'])
        result.append({"text": chunk["text"],
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"], 
                    "semantic_score":score})

    # Sort descending based on semantic_score
    result.sort(key=lambda item: item['semantic_score'], reverse=True)

    return result[:top_k]

def keyword_score(query, text):
    """ This method to provide score on keyword serach 
    query: user request
    text: document in which retriver or serch tobe done
    """
    query_words = set(str(query).lower().split())
    text_words = set(str(text).lower().split())

    if not query_words:
        return 0.0

    matches = (query_words & text_words)

    return len(matches)/len(query_words)



def hybrid_search(query, chunks, top_k=5, semantic_weight=0.7, keyword_weight=0.3):
    """ This method do hybrid search combine for semantic and keyword score 
    and the find the result """

    query_embedding = create_embedding(query)
    result =[]
    for chunk in chunks:
        semantic_score = cosine_similarity(query_embedding, chunk['embedding'])
        exact_match_score = keyword_score(query, chunk['text'])

        combined_score = (semantic_score*semantic_weight + exact_match_score*keyword_weight)

        result.append({"text": chunk["text"],
                    "source": chunk["source"],
                    "chunk_id": chunk["chunk_id"], 
                    "semantic_score":semantic_score,
                    "keyword_score": exact_match_score,
                    "combined_score": combined_score
                    })

        result.sort(key=lambda item:item['combined_score'],reverse=True)

        return result[:top_k]





