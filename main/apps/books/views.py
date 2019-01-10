from django.shortcuts import render, HttpResponse, redirect

# Create your views here.

def index(request):
    response = "this is the index"
    return HttpResponse(response)
