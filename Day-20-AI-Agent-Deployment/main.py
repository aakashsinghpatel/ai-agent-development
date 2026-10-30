from fastapi import FastAPI, HTTPException, Request
from agent import agent
from schema import ChatRequest, ChatResponse
# for moder async HTTP request from python
from httpx import AsyncClient
# to manage context(resources ) of servera
from contextlib import asynccontextmanager
from config import OLLAMA_BASE_URL
import asyncio
from tenacity import retry, stop_after_attempt, wait_exponential
from observability import logger, check_rate_limit
import uuid
import time


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


# chat api: with Reliability: Timeout, retry, rate limiting
@server.post("/chat", response_model=ChatResponse)
async def chat(request: Request, body: ChatRequest):
    request_id = str(uuid.uuid4())
    client_id = request.client.host
    
    if not check_rate_limit(client_id):
        logger.warning("rate_limit_exceeded request_id=%s client=%s",request_id,client_id)
        raise HTTPException(status_code=429,detail="Rate limit exceeded") 
    
    start_time = time.perf_counter()
    logger.info("request_started request_id=%s",request_id)

    try:
        # result = await agent.ainvoke({"messages": [{"role": "user","content": request.message}]})
        
        # Implement timeout machenism for chat request
        result = await asyncio.wait_for(run_agent(body.message), timeout=5)

        answer = result["messages"][-1].content
        
        duration = time.perf_counter() - start_time
        
        logger.info("request_completed request_id=%s duration=%.2fs",request_id, duration)
        
        # return {"answer": result["messages"][-1].content}
        return ChatResponse(answer=answer)
    
    except asyncio.TimeoutError:
            logger.error("request_timeout request_id=%s",request_id)
            raise HTTPException(status_code=504, detail="Agent request timed out")
    
    except Exception as e:
        print("Exception occured: ", e)
        # Below will be return to client as response
        raise HTTPException(status_code=500, detail="Internal server error: Agent execution failed")



# Observability: Make retry machanism for retry max 2 attempt

@retry(
    stop=stop_after_attempt(2),
    wait=wait_exponential(
        multiplier=1,
        min=1,
        max=4
    )
)
async def run_agent(message: str):
    return await agent.ainvoke({"messages": [{"role": "user","content": message}]})
