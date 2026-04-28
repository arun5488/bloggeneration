from typing import TypedDict
from pydantic import BaseModel, Field
from src.bloggeneration import logger

class Blog(BaseModel):
    title: str = Field(default="Title of the blog")
    content: str = Field(default = "content of the blog")

class BlogState(TypedDict):
    topic: str
    blog: Blog
    current_language: str
