1. Created an AI Assistant that response to user query based on current question 
2. No memory or refernce ot previos question.

Libs: 
pip install openai python-loadenv

venv:
    > python -m venv .venv
    > .venv\scripts\activate

model: qwen2:1.7b (Available via ollama: open source tool to run model on local)
    > ollama pull qwen3:1.7b
    > ollam run qwen3:1.7b

openAI: to create connection/client with model so that python program can talk with AI model
dotenv: to load configuration from .env

User :
    AI Assitant: The program that response to use query, summerization etc withoud plan, toll and memory etc.
    Prompt engineering: To sent instruction to AI model to perform task as directed.
    conversion loop: intraction with AI assitant in query-> Process-> respond manner until not stop forfully (As developed in assistant.py)

    1. On questio at a time (hard code questio) <Hello_ai.py>
    2. converstional loop: assistant.py