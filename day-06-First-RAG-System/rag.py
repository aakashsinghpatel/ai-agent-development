from tools import load_documents, create_embedding, cosine_similarity
from openai import OpenAI
from dotenv import load_dotenv 
import os

# step 1: Load Document
document = load_documents()

load_dotenv()
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv('API_KEY'))

# step 2: Create embedding of documents
documents_embedding = {}
for filename, content in document.items():
    documents_embedding[filename] = create_embedding(client=client,content=content)
# print(len(documents_embedding))


# step 3: Create embedding of user question

print("="*40)
print("******** Welcome to RAG AI Assistant*************")
print("="*40)
print("Please ask question. Anytime want to stop conversation enter 'quit'!.")

# Initiate conversation loop
while True:
    # Taking user input
    user_input = input(" You: ")
    if user_input.lower() == 'quit':
        print("Thanks, Good Day!....")
        break
# Step 4: Compare the embeding of question with document and find the best match
    user_embedding = create_embedding(client, user_input)
    best_score  = -1
    best_score_file = ''
    for filename, document_embedding in  documents_embedding.items():
        score = cosine_similarity(user_embedding, document_embedding)

        if best_score < score:
            best_score = score
            best_score_file = filename
    # print(f"Best score: {best_score}")
    # print(f"Best score file: {best_score_file}")


# step 5: Retrive the document based on best match score based on cosine similarity
    retrived_document = document[best_score_file]
    # print("Retrived Document", retrived_document)

# step 6: Create prompt
    prompt = f""" Please answer the question from the following document only.
     Document: {retrived_document}
     Question:{user_input} 
    """

# step 7: Sent prompt to AI model and generate response
    ai_response = client.chat.completions.create(model=os.getenv('MODEL'), messages=[
        {"role":"user", "content":prompt}
    ])
    ai_text = ai_response.choices[0].message.content
    
# step 8: Display the reponse
    print(" AI:",ai_text)