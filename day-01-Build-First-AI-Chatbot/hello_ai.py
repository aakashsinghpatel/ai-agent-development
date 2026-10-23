# lib to communicate with AI model
from openai import OpenAI 
#  to read value of .env file
from dotenv import load_dotenv
# to get acces to os level function
import os

# load the configuration from .env file
load_dotenv()

# Create a client to communicate with ollama model
client  = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))


# # sent message to model and get response
response = client.chat.completions.create(
                                    model=os.getenv("MODEL"), 
                                    messages=[{"role":"user", 
                                               "content":"Please create 50 word story on rain"}])

print(response.choices[0].message.content)