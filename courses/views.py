from django.shortcuts import render
from django.views import View
from . models import Teachers
# Create your views here.

def courses(request):
    return render(request,'courses/sqldata.html')
def dataml(request):
    return render(request,'courses/dsml.html')


