# from unicodedata import name
from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Blog(models.Model):
    writer = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    img = models.CharField(max_length=500)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)

    class Meta:
        ordering = ['-date', 'title']

class Comment(models.Model):
    content = models.TextField(max_length=2500)
    time = models.DateTimeField(auto_now_add=True)
    commentor = models.ForeignKey(User, on_delete=models.CASCADE)
    article = models.ForeignKey(Blog, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-time']