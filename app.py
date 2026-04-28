import uvicorn
from fastapi import FastAPI, Request
from src.bloggeneration.graph.graph_builder import GraphBuilder
from src.bloggeneration.llm.OpenAiLLM import OpenAiLLM
import os 
from dotenv import load_dotenv
from pydantic import BaseModel

load_dotenv()

app = FastAPI()

class BlogRequest(BaseModel):
    topic: str

@app.post("/blogs")
async def create_blogs(payload: BlogRequest):
    topic = payload.topic

    openaillm = OpenAiLLM()
    llm  = openaillm.get_llm()

    graph_builder = GraphBuilder(llm)

    if topic:
        graph = graph_builder.setup_graph(usecase = "topic")
        state = graph.invoke({"topic":topic})
    return {"data": state}


if __name__ == "__main__":
    uvicorn.run("app:app", host = "0.0.0.0", port = 8000, reload = True)
