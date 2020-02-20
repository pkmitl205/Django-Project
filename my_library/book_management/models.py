from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    email = models.EmailField()

class Book(models.Model):
    isbn = models.CharField(
        max_length = 200, 
        primary_key=True, 
        unique=True, 
        null=False) 
    title = models.CharField(max_length = 200)
    author = models.ManyToManyField(Author)
    publisher = models.CharField(max_length = 200)
    price = models.FloatField(default = 0)