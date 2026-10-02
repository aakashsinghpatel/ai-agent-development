# Import all required libs
from openai import OpenAI
from dotenv import load_dotenv
import os

# import planner
from planner import choose_tool

# import tool manager
from tool_manager import execute_tool

# Load the configuration from environment file
load_dotenv()

# Create the client to connect with AI model (qwen3:1.7b)
client = OpenAI(api_key=os.getenv('API_KEY'), base_url=os.getenv("BASE_URL"))

if(client):
    print('Connect with AI modal Stablished!')

print("="* 40)
print("    MY AI Assistant")
print("="* 40)

# Initiate conversation loop
while True:
    # step 1: Taking user input
    user_input = input(" You: ")

    # step 2: check to planner what to next : too?
    tool_name = choose_tool(user_input)

    # Step 3: execute tool with tool manager
    tool_result = None
    if tool_name != 'None': 
        tool_result = execute_tool(tool_name)

    # Step 4: Create Prompt to generate AI Assitant response.
    prompt = f""" 
        Please response to user query.
        with just of tool result.
        user query: {user_input}
        tool result: {tool_result}

        If tool result not available then only use LLM model to response to query in just 10 words.

        Make sure the response looks natural.
        """
    if(user_input.lower() == 'quit'):
        print("Thank for journey, Good Day!..")
        break

    # step 5: Sent prompt to AI assistant and generate Response
    response = client.chat.completions.create(model=os.getenv("MODEL"), 
                                              messages=[{"role":"user", "content":prompt}])

    print(" AI:", response.choices[0].message.content)


    

