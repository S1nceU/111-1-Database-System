# -*- encoding -*-
from django.db import models
from django.contrib import admin

class Maker(models.Model):
    name = models.CharField(max_length=10)
    country = models.CharField(max_length=10) 

    def __str__(self):
        return self.name

class PModel(models.Model):
    maker = models.ForeignKey(Maker, on_delete = models.CASCADE)
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class Product(models.Model):
    pmodel = models.ForeignKey(PModel, on_delete = models.CASCADE,verbose_name="雞雞型號")
    nickname = models.CharField(max_length=15, default = 'testProduct',verbose_name="雞雞名稱")
    description = models.TextField(default='nothing')
    year = models.PositiveIntegerField(default = 2022, verbose_name="雞雞歲數")
    price = models.PositiveIntegerField(default = 0 , verbose_name="雞雞價格")

    def __str__(self):
        return self.nickname

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    description = models.CharField(max_length=20, default='picture')

    def __str__(self):
        return self.description

# from django.db import models


# Create your models here.
class Music(models.Model):
    song = models.TextField()
    singer = models.TextField()
    last_modify_date = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "music"