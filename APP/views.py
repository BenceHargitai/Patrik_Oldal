from multiprocessing import context
from shutil import unregister_unpack_format
from django.shortcuts import render, redirect
from .models import Projekt
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def home_view(request, *args, **kwargs):
    projects =Projekt.objects.all()
    return render(request, "home.html", {'projects' : projects, 'counter' : 1}) 

def adminsite(request, *args, **kwargs):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('home')

    context = {}
    return render(request, 'login.html', context)

