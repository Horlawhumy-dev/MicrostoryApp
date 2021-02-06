from django.db import models

from datetime import datetime


# create models here

class MicroStory(models.Model):
    fullname = models.CharField(max_length=150, unique=True)
    title = models.CharField(max_length=120, unique=True)
    story = models.TextField()
    is_published = models.BooleanField(default=True)
    date_time = models.DateTimeField(default=datetime.now)

 

  

