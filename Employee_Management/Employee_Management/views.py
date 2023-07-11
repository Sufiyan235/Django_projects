from django.db import  models
from django.shortcuts import render,redirect
from emp_app.models import Employee

def employee(request):
    all_emp=Employee.objects.all()
    # print(all_emp)
    context={
        'all_emp':all_emp,
    }

    return render(request,'home.html',context)