from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

def greet(request: HttpRequest):
    query = request.GET.dict()
    name, age = query["name"], query["age"]
    return HttpResponse(f"Hello, {name} of age:{age}")

def post_greet(request):
    return HttpResponse(f"Hello")