"""Projekt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP.views import home_view, login_view, logout_view, staff_view, profile_view, projekt_view, portfolio_view

urlpatterns = [
    path('admin_django/', admin.site.urls),
    path('', home_view, name="home"),
    path('login/',login_view, name="login"),
    path('logout/',logout_view, name="logout"),
    path('portfolio/',portfolio_view, name="portfolio"),
    path('rolunk/',home_view, name="rolunk"),
    path('kapcsolat/',home_view, name="kapcsolat"),
    path('admin/',staff_view, name="admin"),
    path('profil/',profile_view, name="profil"),
    path('projekt/<str:név>/', projekt_view),
]
