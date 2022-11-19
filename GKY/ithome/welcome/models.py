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
    pmodel = models.ForeignKey(PModel, on_delete = models.CASCADE)
    nickname = models.CharField(max_length=15, default = 'testProduct')
    description = models.TextField(default='nothing')
    year = models.PositiveIntegerField(default = 2022)
    price = models.PositiveIntegerField(default = 0)

    def __str__(self):
        return self.nickname

class PPhoto(models.Model):
    product = models.ForeignKey(Product, on_delete= models.CASCADE)
    description = models.CharField(max_length=20, default='picture')

    def __str__(self):
        return self.description