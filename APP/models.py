import imghdr
from nturl2path import url2pathname
from django.db import models
from django.shortcuts import render
# Create your models here.

class Projekt(models.Model):
    név = models.CharField(max_length=30)
    leiras = models.CharField(max_length=300)
    public = models.BooleanField()
    img = models.ImageField()
    url = models.URLField()
    projektszam = models.IntegerField()


    class Meta:
        verbose_name = ("Projekt")
        verbose_name_plural = ("Projektek")

    def __str__(self):
        return self.név

    def Add(post):
        print("POST")
        count = Projekt.objects.count
        Projekt.objects.create(név = post['név'], leiras =post['leiras'], public = post['public'], img = post['img'], url = post['url'], projektszam = count)
        
    # def get_absolute_url(self):
    #     return reverse("Projekt_detail", kwargs={"pk": self.pk})
