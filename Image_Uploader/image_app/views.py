from django.shortcuts import render,redirect
from .forms import ImageUploaderForm
from .models import ImageUploader

# Create your views here.
def  home(request):
    if request.method=='POST':
        form =ImageUploaderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()


    form=ImageUploaderForm()     #displaying Form
    img=ImageUploader.objects.order_by('-date')
    context={
        'form':form,
        'img':img,
    }
    return render(request,'home.html',context)
