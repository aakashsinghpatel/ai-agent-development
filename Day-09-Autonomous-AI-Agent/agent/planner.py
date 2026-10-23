from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(api_key=os.getenv("API_KEY"),base_url=os.getenv("BASE_URL"))

def get_tool_description(tool_list):
    """ Methos to return all list of tools """
    tool_description = ''
    for tool in tool_list:
        tool_description+= f""" 
            Tool Name:{tool.name}
            Tool Description: {tool.description}
         """
    return tool_description

def planner(state, tool_list):
    """ Planner : this will decide what is next action based on current state and action from tool descripto
      """
    available_tools = get_tool_description(tool_list)
    prompt = f"""  
    You are an intelligent Planner.
    Your job is to only decide next action.
    user Request: {state['user_request']}

    Available Tools:
    {available_tools}

    completed action:
    {state['actions']}

    Previous observation:
    {state['observations']}

    Instruction:
        1. Choose only one next action.
        2. Never repeat an action that has already been completed.
        3. Use the observations to decide what is still required.
        4. If the user's request has been completely satisfied, return FINISH.
        5. Return ONLY the tool name or FINISH.
        6. Do not explain your answer.
    """

    response = client.chat.completions.create(model=os.getenv("ASSISTANT_MODEL"),
                                   messages=[{'role':'user', 'content':prompt}])
    
    tool_name = response.choices[0].message.content

    return tool_name