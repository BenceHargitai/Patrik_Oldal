from django.contrib import admin
from .models import Projekt, Kepek, Kapcsolo, Fooldal
from . import models

# Register your models here.

admin.site.register(Kepek)
admin.site.register(Kapcsolo)
admin.site.register(Projekt)
admin.site.register(Fooldal)