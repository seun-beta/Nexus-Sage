from fastapi import FastAPI
from pydantic import BaseModel

from src.rag import rag_client

app = FastAPI()


@app.get("/")
async def healthcheck():
    return {"data": "PONG!"}


class Query(BaseModel):
    query: str


@app.post("/query")
def root(query: Query):
    response = rag_client(query.query)
    return {"data": response}
