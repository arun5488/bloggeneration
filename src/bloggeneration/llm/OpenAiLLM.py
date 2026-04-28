import os
from langchain_openai import ChatOpenAI
from src.bloggeneration import logger
from dotenv import load_dotenv



class OpenAiLLM:
    def __init__(self):
        logger.info("Initializing OpenAiLLM")
        load_dotenv()
        
    def get_llm(self):
        logger.info("Getting LLM")
        self.openai_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(model="gpt-4o-mini", api_key=self.openai_key)
        return self.llm
