from django.db import models

# Create your models here.
class UserAccount(models.Model):
    firstname = models.CharField(max_length=50, unique=True)
    lastname = models.CharField(max_length=50, unique=True)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    password1 = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)

 