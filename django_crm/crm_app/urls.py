from django.urls import path
from. import views
urlpatterns = [
    path("",views.home,name='home'),    
    path("logout/",views.logout_user,name='logout_user'),
    path("register/",views.register_user,name='register'),
    path("details/<int:pk>/",views.details,name='details'),
    path("delete/<int:pk>/",views.delete_record,name='delete'),
    path("add_record/",views.add_record,name='add_record'),
    path("update_record/<int:pk>/",views.update_record,name='update_record'),
]
