from django.shortcuts import redirect
from . models import Customer

def address_required(view_func):
    def wrapper(request,*args,kwarsg):
        if request.user.is_authenticated:
            user=request.user
            customer= Customer.objects.filter(user=request.user)
            if customer:
                return redirect('/checkout')
            else:
                return view_func(request,*args,kwarsg)
        return wrapper