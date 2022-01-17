from email.policy import default
from django.contrib.auth.models import User
from django.db import models
from socket import fromshare



class Book(models.Model):
    price=models.FloatField()
    publisher=models.CharField(max_length=200)
    status=models.BooleanField(default=False)
    
    title=models.CharField(max_length=200)
    author=models.CharField(max_length=200)
    #title = models.TextField()
    cover = models.ImageField(upload_to='myimage')

    def __str__(self):
        return self.title
class Image(models.Model):
 date = models.DateTimeField(auto_now_add=True)  
 photo = models.ImageField(upload_to="myimage/")
 




