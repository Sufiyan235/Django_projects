from django.db import models

# Create your models here.
class Employee(models.Model):
    Name = models.CharField(max_length=20,unique=True)
    Age = models.IntegerField()
    Email= models.EmailField(max_length=300,unique=True)
    Emp_id = models.CharField(max_length=4,unique=True)
    Experience = models.CharField(max_length=20)
    # Resume = models.FileField(upload_to='Emp_Resume')
    Salary = models.CharField(max_length=20)
    Position = models.CharField(max_length=100 , null=True,blank=True)
    Phone=models.CharField(max_length=10)
    Address = models.TextField(max_length=200)
    Joining_Date = models.DateField(auto_now_add=True)
    Photo =models.ImageField(upload_to='Emp_Images/',null=True,blank=True)

 