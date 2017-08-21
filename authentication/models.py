from __future__ import unicode_literals

from django.db import models

# Create your models here.

class LoginForm(models.Model):
	user_name=models.CharField(max_length=250)
	password=models.CharField(max_length=200)



class SignupForm(models.Model):
	full_name=models.CharField(max_length=300)
	pwd=models.CharField(max_length=200)
	cpw=models.CharField(max_length=200)
	email=models.CharField(max_length=300)
	phone_no=models.IntegerField(default=0)



