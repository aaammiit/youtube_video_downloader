from django.db import models

# Create your models here.
class Video_link(models.Model):
    link=models.CharField(max_length=1000)