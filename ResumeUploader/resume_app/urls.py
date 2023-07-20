from django.urls import path
from . import views
urlpatterns = [
    path('add_emp/',views.add_emp,name='add_emp'),
    path('deatils/<int:id>/',views.details,name='details'),
    path("delete/<int:id>/",views.delete,name='delete_emp'),
    path("update/<int:id>/",views.update,name='update_emp'),
    path("do_update/<int:id>/",views.do_update_emp,name='do_update_emp'),
    
]