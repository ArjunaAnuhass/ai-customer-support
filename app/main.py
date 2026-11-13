from fastapi import FastAPI

app = FastAPI(title="AI Customer Support")


@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Health check passed!"}
