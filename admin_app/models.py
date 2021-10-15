from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    img = models.ImageField(upload_to='pics')
    special = models.BooleanField(default=False)
    desc = models.TextField()



class Products(models.Model):
    name = models.CharField(max_length=100)
    desc = models.TextField()
    img = models.ImageField(upload_to='pics')
    price = models.IntegerField()
    offer = models.BooleanField(default=False)
    category = models.ForeignKey(Category,on_delete=models.CASCADE,default=False)

class Cart(models.Model):
    userid = models.ForeignKey(User, on_delete=models.CASCADE)
    pid=models.ForeignKey(Products, on_delete=models.CASCADE)
















