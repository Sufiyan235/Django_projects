from django.shortcuts import render
from resume_app.models import Resume
# Create your views here.
def home(request):
    emps = Resume.objects.all()
    context={
        'emps':emps
    }
    return render(request,'home.html',context)