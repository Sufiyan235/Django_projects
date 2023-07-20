from django.shortcuts import render,redirect
from . models import Resume
# Create your views here.
def add_emp(request):
    if request.method =='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        gender=request.POST['gender']
        phone=request.POST['phone']
        locality=request.POST['locality']
        city=request.POST['city']
        pin=request.POST['pin']
        photo=request.FILES['photo']
        resume=request.FILES['resume']
        join=request.POST['join_date']

        employee=Resume(Name=name,DOB=dob,Email=email,Gender=gender,Locality=locality,City=city,Pin=pin,Resume=resume,Phone=phone,Joining_Date=join,Profile_Photo=photo)
        employee.save()
        return redirect('home')
    return render(request,'add_emp.html')


def details(request,id):
    details=Resume.objects.get(id=id)
    context={
        'details':details,
    }

    return render(request,'details.html',context)



def delete(request,id):
    del_emp=Resume.objects.get(id=id)
    del_emp.delete()
    return redirect('home')


def update(request,id):
    upd_emp=Resume.objects.get(id=id)
    context = {
        'emp':upd_emp
    }
    return render(request,'update_emp.html',context)


def do_update_emp(request,id):

    name=request.POST['name']
    dob=request.POST['dob']
    email=request.POST['email']
    photo=request.FILES['photo']
    gender=request.POST['gender']
    phone=request.POST['phone']
    locality=request.POST['locality']
    resume=request.FILES['resume']
    pin=request.POST['pin']
    join_date=request.POST['join_date']
    city=request.POST['city']

    new_emp=Resume.objects.get(id=id)

    new_emp.Name=name
    new_emp.DOB=dob
    new_emp.Email=email
    new_emp.Profile_Photo=photo
    new_emp.Gender=gender
    new_emp.Phone=phone
    new_emp.Locality=locality
    new_emp.Resume=resume
    new_emp.Pin=pin
    new_emp.Joining_Date=join_date
    new_emp.City=city

    new_emp.save()
    return redirect('home')



