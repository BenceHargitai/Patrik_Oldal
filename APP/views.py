from django.shortcuts import render
from .models import Projekt

# Create your views here.
def home_view(request, *args, **kwargs):
    projects =Projekt.objects.all()
    return render(request, "home.html", {'projects' : projects, 'counter' : 1}) 