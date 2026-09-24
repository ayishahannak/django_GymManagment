from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return HttpResponse("welcome to gym management")

def index(request):
    return render(request, "index.html")


def dashboard(request):
    return render(request, "dashboard.html")


def login(request):
    return render(request, "login.html")