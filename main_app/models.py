# from unicodedata import name
from django.db import models

# Create your models here.



class Blog(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    class Meta:
        ordering = ['-date']