from fastapi import FastAPI
from agent import agent
from requestModel import ChatRequestModel

server = FastAPI(title="Fast API server", version="1.0.0")


@server.post("/chat")
async def chat(request:ChatRequestModel):
    print(request)
    result = await agent.ainvoke({"messages": [{"role": "user","content": request.message}]})
    return {"answer": result["messages"][-1].content}
