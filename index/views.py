from django.shortcuts import render
from django.views import View
from . models import CourseList,Expert
from . form import RegistrationForm
from django.contrib import messages


# Create your views here.
#def index(request):
 #   return render(request,'index/index.html')

class CourseView(View):
    def get(self,request):
        courses = CourseList.objects.all()
        teachers = Expert.objects.all()
        return render(request,'index/index.html',
                      {'courses':courses,'teachers':teachers})
    
class RegistrationView(View):
    def get(self,request):
        form=RegistrationForm()
        return render(request,'index/registration.html',{'form':form})

    def post(self,request):
        form=RegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulations! Registration successfully done.')
            form.save()
        return render(request,'index/registration.html',{'form':form})

    
