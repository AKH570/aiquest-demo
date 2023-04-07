from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from . models import CourseList,Expert,AboutPage,Cart
from django.contrib.auth import views
from . form import RegistrationForm,LoginForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login
from django.http import JsonResponse

from django.http import HttpResponse


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
        return render(request,'courses/bigdata.html',
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
    
class CourseDetailPage(View):
    def get(self,request,pk):
        totalitem=0
        course=CourseList.objects.get(pk=pk)
        already_in_cart = False
        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            already_in_cart=Cart.objects.filter(Q(product=course.id)&Q(user=request.user)).exists()
        return render(request,'courses/course_details.html',{'course':course,'already_in_cart':already_in_cart,'totalitem':totalitem})
    
def AddtoCart(request):
    user=request.user
    course_id =request.GET.get('prod_id')
    product=CourseList.objects.get(id=course_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

def Info_Cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount = 0
        shipping_charge=100
        #total_amt=0
        if cart:
            for i in cart:
                tempamt = i.quantity*i.product.price
                amount +=tempamt
                totalamount = amount+shipping_charge
       # cart_product = [p for p in Cart.objects.all() if p.user==user]
            return render(request,'courses/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount})
    
        else:
            return render(request,'courses/emptycart.html')
        
def plus_cart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity +=1
        c.save()
        amount =0.0
        shipping_amount=100.00
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }

        return JsonResponse(data)

def minus_cart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity -=1
        c.save()
        amount =0.0
        shipping_amount=100.00
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount
        }

        return JsonResponse(data)
    
def remove_cart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.delete()
        amount =0.0
        shipping_amount=100.00
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamount = (p.quantity * p.product.price)
            amount += tempamount
        data={
            'amount':amount,
            'totalamount':amount+shipping_amount
        }

        return JsonResponse(data)