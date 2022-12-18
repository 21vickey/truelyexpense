from django.shortcuts import render

# Create your views here.
def index(request):
    return render (request, 'expense/index.html')


def add_expense(request):
    return render (request, 'expense/add_expense.html')