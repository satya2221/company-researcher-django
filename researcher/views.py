from django.shortcuts import render
from django.views.generic import View
from .methods import generate_queries, research

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        company_name = request.POST.get("company_name")

        queries = []
        
        financial_queries = generate_queries("financial",company_name)
        leadership_queries = generate_queries("leadership",company_name)
        operations_queries = generate_queries("operations",company_name)
        corporate_history_queries = generate_queries("corporate history",company_name)

        queries.extend(financial_queries.get("queries"))
        queries.extend(leadership_queries.get("queries"))
        queries.extend(operations_queries.get("queries"))
        queries.extend(corporate_history_queries.get("queries"))

        context = ""

        for query in queries:
            response = research(query)

            context += f"Query: {query} \nResponse: {response}\n\n"

        return render(request, "index.html")