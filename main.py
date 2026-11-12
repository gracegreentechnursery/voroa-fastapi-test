from fastapi import FastAPI

app = FastAPI(title="Voroa Hosting Test")

@app.get("/")
def home():
    return {
        "status": "success",
        "message": "FastAPI is running on Voroa"
    }

@app.get("/health")
def health():
    return {"status": "healthy"}
