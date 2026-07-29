from fastapi import FastAPI 
from sqlalchemy import text
from app.api.v1.endpoints.cases import router as case_router

from app.db.base import Base
from app.db.session import engine


with engine.connect() as conn:
    conn.execute(text("CREATE EXTENSION IF NOT EXISTS vector"))
    conn.commit()

Base.metadata.create_all(engine)

app = FastAPI(
    title="Crime Intelligence Platform",
    version = "1.0.0",
)


app.include_router(case_router)


@app.get("/")
def root():
    return {
        "message" : "Welcome to the Crime Intelligence Platform",
        "status" : "running"
        }


