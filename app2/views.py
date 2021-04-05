from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Welcome to Index of App2</h1>")

def sample2(request):
    return render(request,"app2/sample2.html")


# Create your views here.
