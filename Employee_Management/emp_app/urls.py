from django.urls import path
from emp_app import views

urlpatterns = [
    path("add_emp",views.add_emp,name='add_emp'),
    path('details/<int:emp_id>/',views.details,name='details'),
    path('delete_emp/<int:emp_id>/',views.delete_emp,name='delete_emp'),
    path('update_emp/<int:emp_id>/',views.update_emp,name='update_emp'),
    path('do_update_emp/<int:emp_id>/',views.do_update_emp,name='do_update_emp'),

]
