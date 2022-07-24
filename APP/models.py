import imghdr
from nturl2path import url2pathname
from pyexpat import model
from django.db import models
from django.shortcuts import render
from ckeditor.fields import RichTextField
# Create your models here.

class Projekt(models.Model):
    id = models.IntegerField(auto_created=True,primary_key=True, editable=False)
    név = models.CharField(max_length=30)
    leiras = RichTextField(blank=True,null=True)
    public = models.BooleanField()
    img = models.ImageField()
    url = models.URLField()

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



class Kapcsolo(models.Model):
    key = models.ForeignKey(Projekt,on_delete=models.CASCADE)
    felirat = models.CharField(max_length=15)

    class Meta:
        verbose_name = ("Kapcsolo")
        verbose_name_plural = ("Kapcsolo")

    def __str__(self):
        return f'{self.key}: {self.felirat}'
        
    @property
    def kepei(self):
        return Kepek.objects.filter(key = self)
    

class Kepek(models.Model):
    key = models.ForeignKey(Kapcsolo, on_delete=models.CASCADE)
    url = models.URLField()

    class Meta:
        verbose_name = ("Kép")
        verbose_name_plural = ("Képek")

    def __str__(self):
        return f'{self.key} - {self.url}'


