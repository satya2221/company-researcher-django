from core.prompt_manager import PromptManager
from pydantic import BaseModel
from .prompts import QUERY_GENERATOR_PROMPT
from .utils import tavily_client

class Queries(BaseModel):
    category: str
    queries: list[str]

def generate_queries(category, company_name):
    pm =PromptManager()
    pm.add_message("system", QUERY_GENERATOR_PROMPT.format(company_name=company_name, category=category))
    pm.add_message("user", "")

    return pm.generate_structure(Queries)

def research(query):
    response = tavily_client.qna_search(query)
    return response