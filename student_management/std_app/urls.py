from django.urls import path
from . import views

urlpatterns = [
    
    path('add_std/',views.add_std,name='add_std'),
    path('delete_std/<int:roll>',views.delete_std,name='delete_std'),
    path('update_std/<int:roll>',views.update_std,name='update_std'),
    path('do_update/<int:roll>',views.do_update,name='do_update'),

]