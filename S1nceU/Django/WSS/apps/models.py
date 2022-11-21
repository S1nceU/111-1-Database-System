from django.db import models
from django.contrib import admin

class SELLER(models.Model):
    username = models.CharField(max_length=10)
    account = models.CharField(max_length=10) 
    member_status = models.BooleanField(default=False)
    password = models.CharField(max_length=10)
    Email = models.EmailField()
    phone = models.CharField(max_length=10)
    ID_number = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class SELLER(models.Model):
    username = models.CharField(max_length=10)
    account = models.CharField(max_length=10) 
    member_status = models.BooleanField(default=False)
    password = models.CharField(max_length=10)
    Email = models.EmailField()
    phone = models.CharField(max_length=10)
    ID_number = models.CharField(max_length=10)
    def __str__(self):
        return self.name

class SELLER(models.Model):
    username = models.CharField(max_length=10)
    account = models.CharField(max_length=10) 
    member_status = models.BooleanField(default=False)
    password = models.CharField(max_length=10)
    Email = models.EmailField()
    def __str__(self):
        return self.name

class SALESREPORT(models.Model):

    sales_results = models.CharField()
    sales_score = models.FloatField()
    user_id = models.ForeignKey(SELLER,verbose_name=)
    def __str__(self):
        return self.name

class SALESREPORT(models.Model):
    label = models.CharField()    
    models.ForeignKey(SELLER,verbose_name=)
    def __str__(self):
        return self.name

class ORDER(models.Model):

    total_price = models.IntegerField()
    order_time = models.DateField()
    address = models.CharField()
    def __str__(self):
        return self.name