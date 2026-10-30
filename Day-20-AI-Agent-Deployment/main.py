from fastapi import FastAPI, HTTPException
from agent import agent
from schema import ChatRequest, ChatResponse
# for moder async HTTP request from python
from httpx import AsyncClient
# to manage context(resources ) of servera
from contextlib import asynccontextmanager
from config import OLLAMA_BASE_URL





# Lifecycle:: 
# APP start -> Initialize resource -> serve  request -> clean up -> close app server
@asynccontextmanager
async def lifespan(app: FastAPI):
    print("Application starting: Do all initialization job MCP connection, DB connection etc")
    # Yiels is boundy after start and before stop app server
    yield
    print("Application shutting down: Cleanup task: Close conenction etc.")

server = FastAPI(title="Fast API server", version="1.0.0",
                #  attached lifespan method to FastAPi
                lifespan=lifespan)

# liveness:: health check : to check application server is live or now
@server.get('/health')
def health():
    return {"status":"ok"}

# Readiness: TO check all service working (LLM, RAG, DB,VS etc)
@server.get('/ready')
async def ready():
    try:
        async with AsyncClient() as client:
            response = await client.get(f"{OLLAMA_BASE_URL}/api/tags")   
            print(response)         
            if response.status_code ==200:
                return {"status": "ready"}
            else:
                return {"status": "not_ready"}

    except Exception as e:
        print("Error occure to connec with ollama: ",e)
        # return {"status": "not_ready"}
        raise HTTPException(status_code=500, detail="Error occured in readyness")

@server.post("/chat", response_model=ChatResponse)
async def chat(request:ChatRequest):
    try:
        result = await agent.ainvoke({"messages": [{"role": "user","content": request.message}]})
        # return {"answer": result["messages"][-1].content}
        return ChatResponse(answer=result['messages'][-1].content)
    except Exception as e:
        print("Exception occured: ", e)
        # Below will be return to client as response
        raise HTTPException(status_code=500, detail="Internal server error: Agent execution failed")


