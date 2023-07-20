from django.contrib import admin

# Register your models here.
from.models import Resume
class ResumeAdmin(admin.ModelAdmin):
    list_display=['id','Name','Joining_Date']

admin.site.register(Resume,ResumeAdmin)