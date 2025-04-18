from django.shortcuts import render
from django.views.generic import View
from .methods import generate_queries

# Create your views here.
class IndexView(View):
    def get(self, request):
        return render(request, "index.html")
    
    def post(self, request):
        company_name = request.POST.get("company_name")

        financial_queries = generate_queries("financial",company_name)
        leadership_queries = generate_queries("leadership",company_name)
        operations_queries = generate_queries("operations",company_name)
        corporate_history_queries = generate_queries("corporate history",company_name)

        print(f"Financial: {financial_queries}")
        print(f"Leadership: {leadership_queries}")
        print(f"Operations: {operations_queries}")
        print(f"Corporate History: {corporate_history_queries}")

        return render(request, "index.html")