from fastapi import FastAPI, HTTPException
from agent import agent
from schema import ChatRequest, ChatResponse

server = FastAPI(title="Fast API server", version="1.0.0")


@server.post("/chat", response_model=ChatResponse)
async def chat(request:ChatRequest):
    try:
        result = await agent.ainvoke({"messages": [{"role": "user","content": request.message}]})
        # return {"answer": result["messages"][-1].content}
        return ChatResponse(answer=result['messages'][-1].content)
    except Exception as e:
        print("Exception occured: ", e)
        # Below will be return to client as response
        raise HTTPException(status_code=500, detail="Internal server erro: Agent execution faile")
