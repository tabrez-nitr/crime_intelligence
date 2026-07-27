from fastapi import FastAPI 


app = FastAPI(
    title="Crime Intelligence Platform",
    version = "1.0.0",
)

@app.get("/")
def root():
    return {
        "message" : "Welcome to the Crime Intelligence Platform",
        "status" : "running"
        }


