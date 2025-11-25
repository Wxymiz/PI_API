from fastapi import FastAPI

app = FastAPI(title="Async Pi Calculator API")

@app.get("/")
def read_root():
    return {"message": "Async Pi Calculator API is running"}
