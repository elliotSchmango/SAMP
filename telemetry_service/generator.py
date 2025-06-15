import random
import time
import json
from datetime import datetime

import random
import time
import json
from datetime import datetime
import requests

#dummy data
def generate_fake_telemetry():
    telemetry = {
        "timestamp": datetime.utcnow().isoformat(),
        "cpu_usage": round(random.uniform(10.0, 90.0), 2),
        "memory_usage": round(random.uniform(20.0, 80.0), 2),
        "disk_error_rate": round(random.uniform(0.0, 5.0), 2),
        "status": random.choice(["OK", "WARN", "ERROR"])
    }
    return telemetry

#updated to send to ml_service
def stream_telemetry(interval=2):
    while True:
        data = generate_fake_telemetry()
        try:
            response = requests.post("http://ml_service:9100/ingest", json=data)
            print(f"Posted: {data} | Status: {response.status_code}")
        except Exception as e:
            print(f"Error sending telemetry: {e}")
        time.sleep(interval)