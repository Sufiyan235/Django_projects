from django.contrib import admin
from .models import Employee

# Register your models here.

class EmployeeAdmin (admin.ModelAdmin):
    list_display=['Name','Position','Joining_Date','Experience']

admin.site.register(Employee,EmployeeAdmin)