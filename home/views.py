from django.shortcuts import render

# Create your views here.


def index(request):
    """view to return to index"""
    return render(request, "home/index.html")
