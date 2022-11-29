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
    # def __str__(self):
    #     return self.username

@admin.register(SELLER)
class SELLERadmin(admin.ModelAdmin):
    list_display = [field.name for field in SELLER._meta.fields]