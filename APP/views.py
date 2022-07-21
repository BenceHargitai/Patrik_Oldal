from cmath import log
from multiprocessing import context
from shutil import unregister_unpack_format
from django.shortcuts import render, redirect
from .models import Projekt
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import Permission, User

# Create your views here.
def home_view(request, *args, **kwargs):
    projects =Projekt.objects.all()
    return render(request, "home.html", {'projects' : projects}) 


def login_view(request, *args, **kwargs):

    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request,username = username, password = password)
        # Megnézni, hogy van-e permission!!
        if user is not None:
            login(request,user)
            print('sikeres')
            return redirect('home')
        else:
            messages.info(request, 'A felhasználónév vagy a jelszó helytelen!')

    context = {}
    if not request.user.is_authenticated:
        return render(request, 'login.html', context)
    else:
        return redirect('home')


def logout_view(request):
    logout(request)
    return redirect('login')



