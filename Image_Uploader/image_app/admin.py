from django.contrib import admin
from .models import ImageUploader
# Register your models here.

class ImageUploaderAdmin(admin.ModelAdmin):
    list_display=['id','image','date']


admin.site.register(ImageUploader,ImageUploaderAdmin)