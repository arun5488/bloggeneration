from src.bloggeneration import logger
from src.bloggeneration.llm.OpenAiLLM import OpenAiLLM
from langgraph.graph import StateGraph, START, END
from src.bloggeneration.state.blogstate import BlogState
from src.bloggeneration.nodes.node import BlogNode

class GraphBuilder:
    def __init__(self, llm):
        logger.info("Initializing GraphBuilder")
        self.llm = llm
        self.graph = StateGraph(BlogState)
        self.blog_node = BlogNode(self.llm)
    def build_topic_graph(self):
        """
        Build the graph to generate the title of the blog
        """
        
        self.graph.add_node("title_creation",self.blog_node.title_creation)
        self.graph.add_node("content_generation",self.blog_node.content_generation)

        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_generation")
        self.graph.add_edge("content_generation", END)

        return self.graph

    def setup_graph(self,usecase):
        if usecase == "topic":
            self.build_topic_graph()
        return self.graph.compile()
