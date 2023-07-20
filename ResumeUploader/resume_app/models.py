from django.db import models

# Create your models here.



class Resume(models.Model):
    Name = models.CharField(max_length=20,unique=True)
    DOB = models.DateField(auto_now=False,auto_now_add=False)
    Email= models.EmailField(max_length=300,unique=True)
    Gender=models.CharField(max_length=100)
    Locality=models.CharField(max_length=100)
    City = models.CharField(max_length=100)
    Pin= models.PositiveIntegerField()
    Resume = models.FileField(upload_to='Emp_Resume')
    Phone=models.PositiveIntegerField()  
    Joining_Date = models.DateField(auto_now_add=True)
    Profile_Photo =models.ImageField(upload_to='Emp_Images',null=True,blank=True)
    