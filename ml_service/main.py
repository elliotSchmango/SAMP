from fastapi import FastAPI, Request
import logging

app = FastAPI()

#simple logging
logging.basicConfig(level=logging.INFO)

@app.post("/ingest")
async def ingest(request: Request):
    data = await request.json()
    logging.info(f"Received telemetry: {data}")
    return {"status": "received"}