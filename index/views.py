from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from . models import CourseList,Expert,AboutPage
from django.contrib.auth import views
from . form import RegistrationForm,LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate,login


# Create your views here.

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

class DjwebaiVie(View):
    def get(self,request):
        c_name = CourseList.objects.filter(course_name='Django for Web & Artificial Intelligence')
        teachers = Expert.objects.all()
        return render(request,'courses/djangowebai.html',
                     {'c_name':c_name})
class BigDataView(View):
    def get(self,request):
        c_name = CourseList.objects.filter(course_name='Big Data Engineer')
        teachers = Expert.objects.all()
        return render(request,'courses/djangowebai.html',
                     {'c_name':c_name})

    
class DeepLearningView(View):
    def get(self,request):
        c_name = CourseList.objects.filter(course_name='Deep Learning for NLP & Computer Vision With Python')
        teachers = Expert.objects.all()
        return render(request,'courses/deeplearning.html',
                     {'c_name':c_name})
class DataAnalystView(View):
    def get(self,request):
        c_name = CourseList.objects.filter(course_name='Data Analyst')
        teachers = Expert.objects.all()
        return render(request,'courses/dataanalyst.html',
                     {'c_name':c_name})
class DataMLView(View):
    def get(self,request):
        c_name = CourseList.objects.filter(course_name='Data Science and ML with Python')
        teachers = Expert.objects.all()
        return render(request,'courses/dataml.html',
                     {'c_name':c_name})
class SqlDsView(View):
    def get(self,request):
        c_name = CourseList.objects.filter(course_name='SQL for Data Science')
        teachers = Expert.objects.all()
        return render(request,'courses/sqldatasc.html',
                     {'c_name':c_name})
    
class AboutView(View):
    def get(self,request):
        about=AboutPage.objects.all()
        return render(request,'about/about.html',{'about':about})