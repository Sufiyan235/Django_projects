from django.db import models

# Create your models here.
class ImageUploader(models.Model):
    image=models.ImageField(upload_to='images',unique=True)
    date=models.DateTimeField(auto_now_add=True)