import asyncio
from openai import OpenAI
from dotenv import load_dotenv
import os 

from agent.mcp_client import connect, disconnect, discover_tool
from graph import build_graph

# Import to resuem after intruppt
from langgraph.types import Command

load_dotenv()

client = OpenAI(base_url=os.getenv("BASE_URL"), api_key=os.getenv("API_KEY"))


async def main():

    mcp_client = await connect()
    tool_list = await discover_tool(mcp_client)
    
    print("Available Tools")
    print("----------------")

    for tool in tool_list:
        print(tool.name)

    print("="*40)
    print("**** My autonomous AI Agent *********")
    print("="*40)

    graph = build_graph(tool_list, mcp_client)

    user_request = input(" You:")

    initial_state = {
        "user_request": user_request,
        "current_step": 0,
        "max_step": 5,
        "actions": [],
        "observations": [],
        "finished": False,
        "action":'',
        "final_answer": ""
    }

    # final_state = graph.invoke(initial_state)

    #  make configuration so that intrupt can be resume in multi user envirnment based on
    # who intruptted
    config = {
        "configurable": {
            "thread_id": "demo-1"
        }
    }
    # Run graph asynchronously
    result = await graph.ainvoke(initial_state,config)

    while True:
        # As there can be multiple interrupt so adde while loop
        # if interrupt has data the continue 
        interrupts = result.get("__interrupt__")
        if not interrupts:
            break
        if interrupts:
            interrupt_data = (interrupts[0].value)

            print("\n==============================")

            print(" HUMAN APPROVAL REQUIRED")

            print("==============================")

            print(interrupt_data["message"])

            print("Tool:",interrupt_data["action"])

            decision = input("\nApprove? (yes/no): ").strip().lower()
                # resume the graph with previous state by pass cammand and config for identification
                
            result = await graph.ainvoke(Command(resume=decision),config)

    print()
    print("Final Answer:")
    print(result['final_answer'])
    await disconnect(mcp_client)
    

if __name__ == "__main__":
    asyncio.run(main())

