# Import all required libs
from openai import OpenAI
from dotenv import load_dotenv
import os

# import all tools
from tools import (get_current_time,generate_password,roll_dice)

# import tool manager
from tool_manager import execute_tool

# Load the configuration from environment file
load_dotenv()

# Create the client to connect with AI model (qwen3:1.7b)
client = OpenAI(api_key=os.getenv('API_KEY'), base_url=os.getenv("BASE_URL"))

if(client):
    print('Connect with AI modal Stablished!')

# System role: to be used to define behaviour of AI model: How AI Assitant should behave
system_roles ={
    "1": "You are a friendly school teacher. Explain every concept using simple language and real-life examples.",
    "2": "You are a senior Python developer. Explain programming concepts clearly and always include Python examples.",
    "3": "You are an experienced travel guide. Recommend places, food, transportation and travel tips.",
    "4": "You are a motivational coach. Encourage the user and give practical advice with a positive attitude.",
    "5": "You are a professional interviewer. Ask one interview question at a time and provide feedback after each answer."
}

# Conversation history list
messages = []

print("="* 40)
print("    MY AI Assistant")
print("="* 40)
print("\nChoose Your Assistant\n")

print("1. Teacher")
print("2. Python Expert")
print("3. Travel Guide")
print("4. Motivational Coach")
print("5. Interviewer")

# Taking choice of assistant role form user 
role_choice = input("\nEnter your choice : ")

# Put first message as System Prompt into conversation History <System Prompt>
messages.append({'role':'system', 'content': system_roles.get(role_choice,"You are an Intelligent AI Assistant.")})
print("Please ask question. Anytime want to stop conversation enter 'quit'!.")

# Initiate conversation loop
while True:
    # Taking user input
    user_input = input(" You: ")

    # Start: Pattern (Matching) based toll integration 
    """ 
    if "time" in user_input.lower() or "clock" in user_input.lower():
        print(" Assistant: ", get_current_time())
        continue

    if "password" in user_input.lower() or "passcode" in user_input.lower():
            print(" Assistant: ", generate_password())
            continue
    
    if "roll" in user_input.lower() or "dice" in user_input.lower():
            print(" Assistant: ", roll_dice())
            continue
 """
    # End: Pattern (Matching) based tool integration 
    
    # Use tool manager to decide tool call and respective result

    tool_result = execute_tool(user_input)

    # Check if tool result has then print and continue else got to AI model call.
    if tool_result:
        print(" Assistant: ", tool_result)
        continue

    if(user_input.lower() == 'quit'):
        print("Thank for journey, Good Day!..")
        break

    # Add user input to conversation history
    messages.append({"role":"user", "content":user_input})
    # Process the User input to AI model
    response = client.chat.completions.create(model=os.getenv("MODEL"), messages=messages)

    if(response.choices[0].message.content):
        # Retried text from Ai response and update on console and conversation history
        ai_res = response.choices[0].message.content
        print(" Assistant: ", ai_res)
        messages.append({"role":"assistant", "content":ai_res})


    

