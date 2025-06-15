import random
import time
import json
from datetime import datetime

def generate_fake_telemetry():
    telemetry = {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_usage": round(random.uniform(10.0, 90.0), 2),
        "memory_usage": round(random.uniform(20.0, 80.0), 2),
        "disk_error_rate": round(random.uniform(0.0, 5.0), 2),
        "status": random.choice(["OK", "WARN", "ERROR"])
    }
    return telemetry

def stream_telemetry(interval=2):
    while True:
        data = generate_fake_telemetry()
        print(json.dumps(data), flush=True)
        time.sleep(interval)