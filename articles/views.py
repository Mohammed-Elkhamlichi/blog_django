from django.shortcuts import render
from django.http import JsonResponse


# Create your views here.
def articles(request):
    return render(request, "articles.html")
