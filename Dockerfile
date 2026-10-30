FROM python:3.12-slim
WORKDIR /app
COPY Day-20-AI-Agent-Deployment/requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY Day-20-AI-Agent-Deployment/ /app/Day-20/
WORKDIR /app/Day-20

EXPOSE 8000

CMD ["uvicorn","main:server",  "--host","0.0.0.0","--port",  "8000"]
