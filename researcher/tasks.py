from .methods import generate_queries, research, generate_business_profile
from huey.contrib.djhuey import task
from core.methods import send_notification
import time

@task()
def process_research(company_name):
    queries = []
    
    send_notification("notification", "Generating Financial Queries")
    financial_queries = generate_queries("financial",company_name)

    send_notification("notification", "Generating Leadership Queries")
    leadership_queries = generate_queries("leadership",company_name)

    send_notification("notification", "Generating Operations Queries")
    operations_queries = generate_queries("operations",company_name)

    send_notification("notification", "Generating Corporate History Queries")
    corporate_history_queries = generate_queries("corporate history",company_name)

    queries.extend(financial_queries.get("queries"))
    queries.extend(leadership_queries.get("queries"))
    queries.extend(operations_queries.get("queries"))
    queries.extend(corporate_history_queries.get("queries"))

    context = ""

    for query in queries:
        send_notification("notification", f"Researching about {query}")
        response = research(query)
        context += f"Query: {query} \nResponse: {response}\n\n"

    send_notification("notification", "Generating Business Profile")
    business_profile = generate_business_profile(context)

    send_notification("final_result", business_profile)