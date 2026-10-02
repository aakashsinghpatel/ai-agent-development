from openai import OpenAI
from dotenv import load_dotenv
import os
# create client
load_dotenv()
client = OpenAI(api_key=os.getenv('API_KEY'), base_url=os.getenv('BASE_URL'))
def choose_tool(user_input):
    """ The AI planner to decide what tool to be called based on user query"""

    prompt = f""" 
    You are an intelligent AI planner.
     Available tools:
      1. get_current_time:
            Tool to return current date or time
    2. roll_dice:
        Return the dice as rolled or number that generate on rolling dice
    3. generate_password:
        return the random genrated password
    
    Return only tool nam ebased on user query.
    if no relavant tool matched then just return 'None'.
    user query: {user_input}
    """
    response = client.chat.completions.create(model=os.getenv('MODEL')
                                              ,messages=[{'role':'user', 'content':prompt}])
    return response.choices[0].message.content.strip()