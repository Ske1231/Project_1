from fastapi import FastAPI

app = FastAPI()

@app.get("/")  # This ensures the root URL works
def read_root():
    return {"message": "Hello, FastAPI is running!"}

@app.post("/run")
def run_task(task: str):
    return {"task": task, "status": "executed"}

@app.get("/read")
def read_file(path: str):
    return {"file": path, "content": "File content here"}



