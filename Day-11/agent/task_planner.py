
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()

client = OpenAI(base_url=os.getenv('BASE_URL'), api_key=os.getenv("API_KEY"))

def decompose_task(user_request):
    """ Method to break user goal into smaller tasks that are like action """
    task_list = []
    prompt = f""" 
        Your are an intelligent task planner.
        Your job is to break user request into smaller independent tasks.

        Rules:
        1. create only necessary task.
        2. put task in execution order.
        3. Each task should be short action.
        4. Each task should be on new line.
        5. Do not number or indexed the task with line number.
        6. Do not explain anything.

        
        CRITICAL RULE:

        Return NO tasks (or "NONE") if the user request belongs to any of the following categories:
        1. Greetings or casual conversation (e.g., "hi", "hello", "how are you?")
        2. Introductions or personal details (e.g., "my name is Pankaj", "I live in Delhi")
        3. Memory questions about past interactions (e.g., "what is my name?", "what did we discuss earlier?")
        4. General knowledge/Q&A questions that can be answered directly without tools (e.g., "what is Machine Learning?", "explain gravity")

        user request: {user_request}
     """
    response = client.chat.completions.create(model=os.getenv('ASSISTANT_MODEL'),
                                                   messages=[
                                                        {'role':"user", 'content':prompt}
                                                   ])
    tasks = response.choices[0].message.content
    print('task decomposer tasks: ',tasks)

    for task in str(tasks).splitlines():
        task_list.append(task)

    return task_list