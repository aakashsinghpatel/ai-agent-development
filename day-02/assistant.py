# import all required libraries
from openai import OpenAI
from dotenv import load_dotenv
import os

# Load all configuration for .env file
load_dotenv()

# Create client with opneAI so that can talk to AI model
client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))

# list of message or conversation history
messages = []

print("="*40)
print("     My AI Assistant")
print("="*40)

while True:
    user_input = input("\n You :: ")
    if(user_input.lower() == 'quit'):
        print("\nGood Bye! Have  a good Day!!")
        break
    # Add user message to conversational memory
    messages.append({"role":"user", "content":user_input})

    # send request to AI model with conversation history having new user message
    response = client.chat.completions.create(model=os.getenv("MODEL"), messages=messages)

    ai_text = response.choices[0].message.content

    # Add AI response/message to conversational memory
    messages.append({"role":"assistant", "content":ai_text})

    print(" AI :: ", ai_text)

    # For debugging purpose 
    print("\n Start ----- conversation History----------")
    for msg in messages:
        # print("\n ", msg)
        print(f"{msg['role'].title()}: {msg['content']}")
    print("\n End ----- conversation History----------")
