from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def home(request):
    return render(request,'index.html')

def register(request):
    return render(request,'reg.html')    