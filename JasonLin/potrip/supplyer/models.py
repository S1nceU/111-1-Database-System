from django.db import models
from django.contrib import admin
class User(models.Model):
	user_name = models.CharField(max_length = 20) # 攤販的名稱
	email = models.CharField(max_length = 10) # 攤販店家的名稱
	nickname = models.CharField(max_length = 20) # 攤販的電話號碼

	def __str__(self):
	    return self.user_name
