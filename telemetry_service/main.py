from fastapi import FastAPI
from contextlib import asynccontextmanager
from generator import stream_telemetry
import threading

@asynccontextmanager
async def lifespan(app: FastAPI):
    t = threading.Thread(target=stream_telemetry, daemon=True)
    t.start()
    yield #wait for app to shutdown

app = FastAPI(lifespan=lifespan)

@app.get("/")
def health_check():
    return {"status": "telemetry_service running"}