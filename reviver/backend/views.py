from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render (request, "home.html")

def add(request):
    return render (request, "add.html")
def delete(request):
    return render (request, "delete.html")

def delete(request):
    return render (request, "edit.html")

# Create your views here.
