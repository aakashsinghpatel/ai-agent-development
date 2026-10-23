from openai import OpenAI
from dotenv import load_dotenv
import os


load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

print("="*40)
print("     My AI Assistant")
print("="*40)

while True:
    user_input = input("\n You :: ")
    if(user_input.lower() == 'quit'):
        print("\nGood Bye! Have  a good Day!!")
        break

    response = client.chat.completions.create(model=os.getenv("MODEL"), messages=[
        {"role":"user", "content":user_input}
    ])
    print(" AI :: ", response.choices[0].message.content)