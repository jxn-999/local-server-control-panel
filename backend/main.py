from fastapi import FastAPI

server_running = False

app = FastAPI()
@app.get("/")
def read_root():
    return {"was geht mein bester"}


@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/status")
def status():
    if server_running:
        return {"running": True}
    else:
        return {"running": False}
    
@app.post("/start")
def start_server():
    global server_running
    server_running = True
    return {
  "success": True,
  "running": True
  }
  
    
@app.post("/stop")
def stop_server():
    global server_running
    server_running = False
    return {
  "success": True,
  "running": False
  }
