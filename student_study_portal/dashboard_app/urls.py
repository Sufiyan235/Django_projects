from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    
    #Notes
    path("notes/",views.notes,name='notes'),
    path("delete_note/<int:id>/",views.delete_note,name='delete_note'),
    path("notes_detail/<int:pk>/",views.NotesDetailView.as_view(template_name = 'notes_detail.html'),name="notes_detail"),

    # homework
    path("homework/",views.homework,name='homework'),
    path("update_homework/<int:pk>/",views.update_homework,name='update_homework'),
    path("del_homework/<int:pk>/",views.delete_homework,name='del_homework'),

    # Youtube
    path('youtube/',views.youtube,name='youtube'),

    # to-do
    path("todo/",views.todo,name='todo'),
    path("update_todo/<int:pk>/",views.update_todo,name='update_todo'),
    path("del_todo/<int:pk>/",views.delete_todo,name='del_todo'),

    # books
    path("books/",views.books,name='books'),

    # dictionary
    path('dictionary/',views.dictionary,name='dictionary'),

    # wiki
    path('wiki/',views.wiki,name='wiki'),

    #convrsion
    path("conversion",views.conversion,name='conversion'),

    
    
    
]