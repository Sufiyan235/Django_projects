from django.shortcuts import render,redirect
from emp_app.models import Employee
# Create your views here.
def add_emp(request):

    if request.method=="POST":
        name = request.POST['name']
        age = request.POST['age']
        email = request.POST['email']
        emp_id = request.POST['emp_id']
        experience = request.POST['experience']
        # resume = request.POST['resume']
        salary = request.POST['salary']
        position = request.POST['position']
        phone = request.POST['phone']
        address = request.POST['address']
        join_date = request.POST['join_date']
        photo = request.POST.get('photo')
        
        emp = Employee(Name=name,Age=age,Email=email,Emp_id=emp_id,Experience=experience,Salary=salary,Position=position,Phone=phone,Address=address,Joining_Date=join_date,Photo=photo)
        emp.save()

        return redirect('employee')
    return render(request,'add_emp.html')


def details(request,emp_id):
    emp=Employee.objects.get(id=emp_id)
    context ={
        'emp':emp
    }
    return render(request,'details.html',context)



def delete_emp(request,emp_id):
    del_emp=Employee.objects.get(id=emp_id)
    del_emp.delete()

    return redirect('employee')


def update_emp(request,emp_id):
    update_emp=Employee.objects.get(id=emp_id)
    context= {
        'emp':update_emp
    }

    return render (request,'update.html',context)

def do_update_emp(request,emp_id):

    n_name=request.POST['name1']
    n_age=request.POST['age1']
    n_email=request.POST['email1']
    n_emp_id=request.POST['emp_id1']
    n_phone=request.POST['phone1']
    n_position=request.POST['position1']
    n_experience=request.POST['experience1']
    # n_resume=request.POST['resume']
    n_salary=request.POST['salary1']
    n_address=request.POST['address1']
    n_photo=request.POST['photo1']
    n_join_date=request.POST['join_date1']


    new_emp=Employee.objects.get(id=emp_id)

    new_emp.Name=n_name
    new_emp.Age=n_age
    new_emp.Email=n_email
    new_emp.Phone=n_phone
    new_emp.Emp_id=n_emp_id
    new_emp.Position=n_position
    new_emp.Experience=n_experience
    # new_emp.Resume=n_resume
    new_emp.Salary=n_salary
    new_emp.Address=n_address
    new_emp.Photo=n_photo
    new_emp.Joining_Date=n_join_date

    new_emp.save()
    return redirect("employee")



    
    
    