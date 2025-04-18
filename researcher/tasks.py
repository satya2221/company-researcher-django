from .methods import generate_queries, research, generate_business_profile
from huey.contrib.djhuey import task
from core.methods import send_notification
import time

@task()
def process_research(company_name):
    queries = []
    
    time.sleep(5)
    send_notification("test", "test notification 1")

    time.sleep(5)
    send_notification("test", "test notification 2")

    time.sleep(5)
    send_notification("test", "test notification 3")
    # financial_queries = generate_queries("financial",company_name)
    # leadership_queries = generate_queries("leadership",company_name)
    # operations_queries = generate_queries("operations",company_name)
    # corporate_history_queries = generate_queries("corporate history",company_name)

    # queries.extend(financial_queries.get("queries"))
    # queries.extend(leadership_queries.get("queries"))
    # queries.extend(operations_queries.get("queries"))
    # queries.extend(corporate_history_queries.get("queries"))

    # context = ""

    # for query in queries:
    #     response = research(query)

    #     context += f"Query: {query} \nResponse: {response}\n\n"

    # business_profile = generate_business_profile(context)

    # print(business_profile)