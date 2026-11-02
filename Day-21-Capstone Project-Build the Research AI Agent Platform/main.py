from fastapi import FastAPI

from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifecycle(app: FastAPI):
    print("Inializing all work.")
    yield
    print("closing all the conencttion")


app = FastAPI(title="AI agent Application", version="1.0.0", lifespan= lifecycle)

#  it is to server statuc files
# attache another ASGI application to a specific URL path. (cretae rout of it)
app.mount('/static', StaticFiles(directory="frontend"),name="static")

@app.get('/')
async def home():
    print("Enter home")
    return FileResponse('frontend/index.html')

@app.get('/health')
def health():
    return {"health": "OK"}