from fastapi import FastAPI
from agent import agent
from schema import ChatRequest, ChatResponse

server = FastAPI(title="Fast API server", version="1.0.0")


@server.post("/chat", response_model=ChatResponse)
async def chat(request:ChatRequest):
    print(request)
    result = await agent.ainvoke({"messages": [{"role": "user","content": request.message}]})
    # return {"answer": result["messages"][-1].content}
    return ChatResponse(answer=result['messages'][-1].content)
