from unicodedata import category
from urllib import request
from django.shortcuts import render
from django.urls import is_valid_path
from django.views import View
from numpy import product
from .models import Cart,Customer,Product,OrderPlaced
from .forms import CustomerRegistrationForm, MyPasswordChangeForm
from django.contrib import messages
# def home(request):
#  return render(request, 'app/home.html')

class ProductView(View):
    def get(self,request):
        topware=Product.objects.filter(category='TW')
        bottomwares=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        return render(request ,'app/home.html',{'topware':topware,'bottomwares':bottomwares,'mobiles':mobiles})
# def product_detail(request):
#  return render(request, 'app/productdetail.html')

class ProductDetailsView(View):
    def get(self,request,pk):
        product=Product.objects.get(pk=pk)
        return render(request, 'app/productdetail.html',{'product':product})

def add_to_cart(request):
 return render(request, 'app/addtocart.html')

def buy_now(request):
 return render(request, 'app/buynow.html')

def profile(request):
 return render(request, 'app/profile.html')

def address(request):
 return render(request, 'app/address.html')

def orders(request):
 return render(request, 'app/orders.html')

 

def mobile(request,data=None):
    if data==None:
        mobiles=Product.objects.filter(category='M')
    elif data=='MI' or data=='vivo' or data=='jio' or data=='realme':
        mobiles=Product.objects.filter(category='M').filter(brand=data)
    elif data=='below':
        mobiles=Product.objects.filter(category='M').filter(discounted_price__lt=10000)
    else:
        mobiles=Product.objects.filter(category='M').filter(discounted_price__gt=10000)

    return render(request, 'app/mobile.html',{'mobiles':mobiles})



class CustomerRegistrashionView(View):
    def get(self,request):
        form=CustomerRegistrationForm()
        return render(request,'app/customerregistration.html',{'form':form})

    def post(self,request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request,'Congratulashion!! Registered SuccessFully')
            form.save()
        return render(request,'app/customerregistration.html',{'form':form})

def checkout(request):
 return render(request, 'app/checkout.html')
