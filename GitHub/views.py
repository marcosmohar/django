from django.shortcuts import render
import requests
from .functions import repositories

# Create your views here.
def index(request):
    return render(request, 'index.html', {'name':'Marcos GitHub'})

def home(request):
    return render(request, 'home.html', {})

def repos(request, subject=None):
    if subject is None:
        pass
    else:
        repos = repositores(subject)
    return render(request, 'repositories.html', {'repos':repos})

