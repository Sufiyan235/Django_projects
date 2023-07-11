from django.contrib import admin
from std_app.models import Student
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display =['Name','Roll','Address','id']
admin.site.register(Student,StudentAdmin)