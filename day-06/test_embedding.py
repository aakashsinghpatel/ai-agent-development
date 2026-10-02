

from openai import OpenAI
from similarity import cosine_similarity

# Cree client for connection with ollama model
client = OpenAI(base_url="http://localhost:11434/v1", api_key='ollama')

embedding_txt_1 = client.embeddings.create(model='nomic-embed-text', 
                                              input="What is python language")

embedding_response_1 = embedding_txt_1.data[0].embedding
print(type(embedding_response_1))
print(len(embedding_response_1))

embedding_txt_2 = client.embeddings.create(model='nomic-embed-text', 
                                              input="What is programming language")

embedding_response_2 = embedding_txt_2.data[0].embedding
print(type(embedding_response_2))
print(len(embedding_response_2))

embedding_txt_3 = client.embeddings.create(model='nomic-embed-text', 
                                              input="Pizza is delicious")

embedding_response_3 = embedding_txt_3.data[0].embedding
print(type(embedding_response_3))
print(len(embedding_response_3))

""" test cosine similarity: Evaluare similirity score """
print(f"Similarity score of between 'What is python language' and " \
"'What is programming language' : {}",cosine_similarity(embedding_response_1, embedding_response_2))

print(f"Similarity score of between 'What is python language' and " \
"'Pizza is delicious food' : {}",cosine_similarity(embedding_response_1, embedding_response_3))




