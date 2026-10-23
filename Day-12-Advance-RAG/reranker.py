
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))


def rerank(query, candidates, top_k):
    """ This method will rank the candidate(Return chunks from retriver (Semntic/exact/hybrid searck))
    Based on relevance of of each to query"""
    result = []

    for candidate in candidates:
        prompt=f""" 
            You are a document relevance evaluator.

            User Query:
            {query}

            Document:
            {candidate["text"]}
            Give a relevance score from 0 to 100.

            100 = directly answers the query
            0 = completely irrelevant

            Return ONLY the number.
         """
        response = client.chat.completions.create(model=os.getenv("ASSISTANT_MODEL"), 
                                                  messages= [{
                                                        "role": "user",
                                                        "content": prompt
                                                        }], temperature=0)
        score_text = response.choices[0].message.content
        try:
            score = float(score_text)
        except ValueError:
            score = 0

        result.append({
            **candidate,
            "rerank_score": score
        })

        result.sort(key=lambda item:item['rerank_score'],reverse=True)

        return result[:top_k]