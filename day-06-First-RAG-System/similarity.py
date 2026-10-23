
import numpy as np
def cosine_similarity(vector1, vector2):
    """ Tool to find cosine similarity or similarity score between two vector """
    
    v1 = np.array(vector1)
    v2 = np.array(vector2)
    # Calculate dot product and norms (magnitudes)
    dot_product = np.dot(v1, v2)
    norm_a = np.linalg.norm(v1)
    norm_b = np.linalg.norm(v2)

    # Compute cosine similarity
    cosine_sim = dot_product / (norm_a * norm_b)
    return cosine_sim
