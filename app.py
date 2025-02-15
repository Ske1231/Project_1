from fastapi import FastAPI
import os

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to DataWorks API"}

@app.post("/run")
def run_task(task: str):
    # Dummy implementation, replace with actual logic
    return {"status": "success", "task": task}

@app.get("/read")
def read_file(path: str):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
        return {"file_content": content}
    else:
        return {"error": "File not found"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
