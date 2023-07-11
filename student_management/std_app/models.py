from django.db import models

# Create your models here.
class Student(models.Model):
    Name = models.CharField(max_length=50)
    Roll = models.CharField(max_length=2)
    Address = models.TextField(max_length=200)
    Email = models.EmailField(max_length=100)
    Phone = models.CharField(max_length=10)