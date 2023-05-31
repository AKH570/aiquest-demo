from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponseRedirect
from . models import CourseList,Expert,AboutPage,Cart,Customer,Contact,ContactMsg
from django.contrib.auth import views
from . form import RegistrationForm,LoginForm,CustomerForm,ContactForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth import authenticate,login
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

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
        return redirect('/regi',{'form':form}) #redirect func clear this existing data after save

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
        product=CourseList.objects.get(pk=pk)
        already_in_cart = False
        if request.user.is_authenticated:
            totalitem= len(Cart.objects.filter(user=request.user))
            already_in_cart=Cart.objects.filter(Q(product=product.id)&Q(user=request.user)).exists()
        return render(request,'courses/course_details.html',{'product':product,'already_in_cart':already_in_cart,'totalitem':totalitem})

@login_required  
def AddtoCart(request):
    user=request.user
    course_id =request.GET.get('prod_id')
    product=CourseList.objects.get(id=course_id)
    Cart(user=user,product=product).save()
    return redirect('/cart')

@login_required 
def Info_Cart(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        #totalitem=len(cart)
        totalitem=0
        amount = 0
        shipping_charge=100
        cart_product = [p for p in Cart.objects.all() if p.user==user] #List Comprehension
        if cart_product:
            for p in cart_product:
                tempamt = p.quantity*p.product.price
                amount +=tempamt
                totalamount = amount+shipping_charge
                totalitem += p.quantity
            #return HttpResponse(tempamt)
            #exit()
            return render(request,'courses/addtocart.html',{'carts':cart,'totalamount':totalamount,'amount':amount,'totalitem':totalitem})
        else:
            return render(request,'courses/emptycart.html')
        
def plus_cart(request):
    if request.method=='GET':
        prod_id = request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id)& Q(user=request.user))
        c.quantity +=1
        c.save()
        amount =0.0
        totalitem=0
        shipping_amount=100.00
        cart_product=[p for p in Cart.objects.all() if p.user==request.user]
        for p in cart_product:
            tempamt = (p.quantity * p.product.price)
            amount += tempamt
            totalitem += p.quantity
        data={
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':amount+shipping_amount,
            'totalitem':totalitem
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
            tempamt = (p.quantity * p.product.price)
            amount += tempamt
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
            tempamt = (p.quantity * p.product.price)
            amount += tempamt
        data={
            'amount':amount,
            'totalamount':amount+shipping_amount
        }

        return JsonResponse(data)

def checkout(request):
    if request.user.is_authenticated:
        user=request.user
        cart=Cart.objects.filter(user=user)
        
        custaddr_already_exist=False
        if request.user.is_authenticated:
            customer= Customer.objects.filter(user=request.user)
            custaddr_already_exist= Customer.objects.filter(user=request.user).exists()
        totalcourses=0
        amount = 0
        shipping_charge=100
        cart_product = [p for p in Cart.objects.all() if p.user==user] #List Comprehension
        if cart_product:
            for p in cart_product:
                tempamt = p.quantity*p.product.price
                amount +=tempamt
                totalamount = amount+shipping_charge
                totalcourses += p.quantity
            return render(request,'courses/checkout.html',{'carts':cart,'totalamount':totalamount,'totalcourses':totalcourses,'customer':customer,'custaddr_already_exist':custaddr_already_exist})
        else:
            return render(request,'courses/emptycart.html')

class AddressView(View):
    def get(self, request):
        address = CustomerForm()
        return render(request,'courses/address.html',{'addrss':address})

    def post(self, request):
        if (request.method=='POST'):
            adr = CustomerForm(request.POST)
            if adr.is_valid():
                user=request.user
                nm=adr.cleaned_data['name']
                ds=adr.cleaned_data['district']
                th=adr.cleaned_data['thana']
                vi=adr.cleaned_data['villorroad']
                cn=adr.cleaned_data['country']
                ph=adr.cleaned_data['phone']
                zp=adr.cleaned_data['zipcode']

                addr=Customer(user=user,name=nm,district=ds,thana=th,villorroad=vi,country=cn,phone=ph,zipcode=zp)
                addr.save()
                messages.success(request, 'Congratulations! Profile Updated Successfully')
        #return redirect('/checkout',{'adr':adr})
        return render(request,'courses/address.html',{'adr':adr})
#payment_done
def payment(request):
    user = request.user
    if Customer.objects.filter(user=request.user).exists()==True:
        return render(request,'courses/orders.html')
    else:
        return render(request,'courses/address.html')



class ContactUs(View):       
        def get(self,request):
            msg=ContactForm()
            contact=Contact.objects.all()
            return render(request,'index/contact.html',{'msg':msg,'contact':contact})
        def post(self, request):
            if request.method=='post':
                msg=ContactForm(request.POST)
                if msg.is_valid():
                    name=msg.cleaned_data['name']
                    email=msg.cleaned_data['email']
                    course=msg.cleaned_data['course_name']
                    message=msg.cleaned_data['message']

                    msgsave=ContactMsg(name=name,email=email,course=course,message=message)
                    msgsave.save()
                    messages.success(request,'Thank you! Your message successfully send.')
                    return HttpResponseRedirect('/contact',{'msg':msg})
            

    
