from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignUpForm,AddRecordForm
from .models import Records
# Create your views here.
def home(request):
    records = Records.objects.all()
    context = {
        'records':records
    }

    #check to see if logging in
    if request.method == 'POST':
        username = request.POST['username']
        passwd = request.POST['password']
        user = authenticate(request,username=username,password=passwd)
        if user is not None:
            login(request,user)
            messages.success(request,'You have logged in!!')
            return redirect('home')
        else:
            messages.error(request,' ERROR! Check Your credentials again!!')
            return redirect('home')
        
    else:
        return render(request,'home.html',context)





def logout_user(request):
    logout(request)
    messages.success(request,'You have been logged out....')
    return redirect('home')


def register_user(request):
    if request.method =='POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password1 = form.cleaned_data['password1']

            user = authenticate(request,username=username,password=password1)
            login(request,user)
            messages.success(request,'You Have Been Registered Sucessfully!!!')
            return redirect('home')

    else:
        form = SignUpForm() # here no req.post cuz here they havent filled the form they want to fill the form.
        context = {
            'form':form
        }
        return render(request,'register.html',context)
    return render(request,'register.html',{'form':form})



def details(request,pk):
    if request.user.is_authenticated:
        record = Records.objects.get(id=pk)
        context ={
            'record':record,
        }
        return render(request,'details.html',context)
    else:
        messages.error(request,'You must be logged in to see the record ')
        return redirect('home')
    

def delete_record(request,pk):
    if request.user.is_authenticated:
        record = Records.objects.get(id=pk)
        record.delete()
        messages.success(request,'Record Deleted Successfully!!!')
        return redirect('home')
    else:
        messages.error(request,'You must be logged in to delete a record ')
        return redirect('home')



def add_record(request):
    form = AddRecordForm(request.POST  or None)
    if request.user.is_authenticated:
        if request.method =='POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request,'Record Added Successfully!!! ')
                return redirect('home')
        return render(request,'add_record.html',{'form':form})
    else:
        messages.success(request,'You must be Loggend in ....')
        return redirect('home')


def update_record(request,pk):
    if request.user.is_authenticated:
        record = Records.objects.get(id=pk)
        form = AddRecordForm(request.POST  or None,instance=record)# instace will fill the fields with data 
        if form.is_valid():
            form.save()
            messages.success(request,'Record Has Been updated!!')
            return redirect('home')
        return render(request,'update_record.html',{'form':form})
    else:
        messages.success(request,'You must be Loggend in ....')
        return redirect('home')

    
    