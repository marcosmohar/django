from django.shortcuts import render
import requests
from .models import Repositories

# Create your views here.
def index(request):
    return render(request, 'index.html', {'name':'Marcos GitHub'})

def home(request):
    return render(request, 'home.html', {})

def repositories(request, subject=None):
    if subject is None:
        repos = Repositories.objects.all()
    else:
        repos = Repositories.objects.filter(subject=subject)
    return render(request, 'repositories.html', {'repos':repos})

