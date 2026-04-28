from src.bloggeneration import logger
from src.bloggeneration.state.blogstate import BlogState

class BlogNode:
    """
    a class to represent the blog node 
    """

    def __init__(self, llm):
        self.llm = llm 

    def title_creation(self, state: BlogState):
        """
        create title for the blog
        """
        logger.info("Creating title for the blog")
        if "topic" in state and state["topic"]:
            prompt = """
            you are an expert blog content writer. Use MD foramtting. Generate a blog title for the topic {topic}.
            This title should be creative and SEO friendly.
            """
            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)

            return {"blog":{"title":response.content}}
    
    def content_generation(self, state: BlogState):
        """
        generate the content for the blog
        """
        logger.info("Inside content_generation")
        if "topic" in state and state["topic"]:
            prompt = """ You are an expert blog content writer. Use MD formatting. 
            Generate a detailed blog content with detailed breakdown for the topic {topic}
            """
            system_prompt = prompt.format(topic = state["topic"])
            response = self.llm.invoke(system_prompt)
            return {"blog":{"title":state["blog"]["title"], "content":response.content}}
            
