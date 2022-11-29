from django.db import models

# Create your models here.
class SELLER(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    account = models.CharField(max_length=10) 
    member_status = models.BooleanField(default=False)
    password = models.CharField(max_length=10)
    Email = models.EmailField()
    phone = models.CharField(max_length=10)
    ID_number = models.CharField(max_length=10)
    address = models.CharField(max_length=20)

class CUSTOMER(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    account = models.CharField(max_length=10) 
    member_status = models.BooleanField(default=False)
    password = models.CharField(max_length=10)
    Email = models.EmailField()
    phone = models.CharField(max_length=10)
    ID_number = models.CharField(max_length=10)

class ADMIN(models.Model):
    user_id = models.CharField(max_length=10)
    username = models.CharField(max_length=10)
    account = models.CharField(max_length=10) 
    member_status = models.BooleanField(default=False)
    password = models.CharField(max_length=10)
    Email = models.EmailField()