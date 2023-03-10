from django.shortcuts import render
from django.views import View
from . models import Product
from courses.models import Teachers

# Create your views here.

def about(request):
    return render(request,'about/about.html')


class ProductView(View):
    def get(self, request):
        product = Product.objects.all()
        return render(request,'index/index.html',{'product':product})


class TeacherView(View):
    def get (self, request):
        teachers= Teachers.objects.all()
        return render (request,'index/index.html',{'teachers':teachers})
