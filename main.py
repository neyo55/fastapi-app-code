from fastapi import FastAPI
import os
import socket

app = FastAPI()

@app.get("/")
def read_root():
    hostname = socket.gethostname()
    
    # Grab the variables from the Kubernetes environment
    environment = os.getenv("APP_ENVIRONMENT", "Unknown Environment")
    api_key = os.getenv("SECRET_API_KEY", "No Key Provided")

    return {
        "message": "Hello from FastAPI!",
        "version": "3.0 - The Config & Secrets Update",
        "pod_name": hostname,
        "environment": environment,
        "api_key_status": api_key, 
        "status": "Unkillable App is Running"
    }