from django.contrib import admin
from .models import Notes,Homework,Todo

# Register your models here.
class NotesAdmin(admin.ModelAdmin):
    list_display=['user','title']
admin.site.register(Notes,NotesAdmin)


class HomeworkAdmin(admin.ModelAdmin):
    list_display=['user','title','due']
admin.site.register(Homework,HomeworkAdmin)

class TodoAdmin(admin.ModelAdmin):
    list_display=['user','title']
admin.site.register(Todo,TodoAdmin)