from django.shortcuts import render,redirect
from .models import Student
# Create your views here.

def add_std(request):
    if request.method=="POST":
        phone=request.POST['phone']
        name=request.POST['name']
        roll=request.POST['roll']
        address=request.POST['address']
        email=request.POST['email']

        stud = Student(Name=name,Roll=roll,Email=email,Address=address,Phone=phone)
        stud.save()

        return redirect("home")

    return render(request,'add_std.html')


def delete_std(request,roll):
    std = Student.objects.get(Roll=roll)
    std.delete()

    return redirect("home")


def update_std(request,roll):
    student = Student.objects.get(Roll=roll)
    context={
        'student':student
    }
    return render(request,'update_std.html',context)


def do_update(request,roll):

    new_name = request.POST['name']
    new_roll = request.POST['roll']
    new_email = request.POST['email']
    new_address = request.POST['address']
    new_phone = request.POST['phone']

    std = Student.objects.get(Roll=roll)

    std.Name=new_name
    std.Roll=new_roll
    std.Address=new_address
    std.Email=new_email
    std.Phone=new_phone

    std.save()
    return redirect('home')
