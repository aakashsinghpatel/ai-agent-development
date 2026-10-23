import sqlite3
from openai import OpenAI
from dotenv import load_dotenv
import os
import json
import numpy as np

load_dotenv()

DATABASE= 'memory.db'

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

def create_database():
    """ Method to create table into DATABSE """
    # conenct to DB
    connection = sqlite3.connect(DATABASE)
    # get controller as cursor to tak to DB
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTs MEMORIES(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_message TEXT,
        assistant_message TEXT,
        embedding TEXT,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        ) """)
    connection.commit()
    connection.close()

def create_embedding(text):
    """ Method to create embedding of text """
    resposne = client.embeddings.create(model=os.getenv("EMBEDDING_MODEL"), input=text)
    return resposne.data[0].embedding

def save_memory(user_message, assistant_message):
    """ Save user message, assitant message with enbedding into memory """
    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    text = user_message + "\n"+ assistant_message
    embedding = create_embedding(text)
    cursor.execute(""" 
        INSERT INTO memories(user_message, assistant_message, embedding) 
        values(?, ?, ?)
     """, (user_message, assistant_message, json.dumps(embedding)))

    connection.commit()
    connection.close()


def cosine_similarity_score(embedding1, embedding2):
    """ Method to get similarity score between two embedding """
    v1 = np.array(embedding1)
    v2 = np.array(embedding2)
    return np.dot(v1, v2) / (
        np.linalg.norm(v1) *
        np.linalg.norm(v2)
    )


def search_semantic_memories(user_request, top_k=3, threshold=0.3):
    """ Method to get top n sementically matched assistant message from memory """

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()
    text_embedding = create_embedding(user_request)
    cursor.execute("SELECT user_message, assistant_message, embedding, created_at from memories")
    rows = cursor.fetchall()
    # print("All rows of DB:" )
    top_matched_rows =[]
    for row in rows:
        user_message, assistant_message, embedding_json, created_at  = row
        memory_embedding = json.loads(embedding_json)
        # print(f"{user_message}, {assistant_message}")
        similarity_score = cosine_similarity_score(text_embedding ,memory_embedding)

        if similarity_score >= threshold:
            top_matched_rows.append({
                "user_message": user_message, 
                "assistant_message":assistant_message,
                "created_at": created_at,
                "score": similarity_score
            })
    top_matched_rows.sort(key= lambda item : item['score'], reverse=True)

    # print("\nMatched rows:\n", top_matched_rows)
    return top_matched_rows[:top_k]


def save_semanctic_meaning(fact):
    fact_embedding = create_embedding(fact)

    connection = sqlite3.connect(DATABASE)
    cursor = connection.cursor()

    cursor.execute("""Insert into memories(user_message,assistant_message ,embedding) 
                values(?,?,?)""", (fact,"", json.dumps(fact_embedding)))

    connection.commit()
    connection.close()



