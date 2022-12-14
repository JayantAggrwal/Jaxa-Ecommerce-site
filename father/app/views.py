from django.shortcuts import render
from django.views import View
from .models import User,Customer,Product,Cart,OrderPlaced
from .forms import CustomerRegistrationForm
from django.contrib import messages

# def home(request):
#  return render(request, 'app/home.html')

# class based view makiing home

class HomeView(View):
    def get(self, request):
        topwears=Product.objects.filter(category='TW')
        bottomwears=Product.objects.filter(category='BW')
        mobiles=Product.objects.filter(category='M')
        return render(request, 'app/home.html',{'topwears': topwears, 'bottomwears': bottomwears,'mobile':mobiles})


# def product_detail(request):
#  return render(request, 'app/productdetail.html')
class ProductDetailView(View):
    def get(self, request,id):
        product=Product.objects.get(id=id)
        return render(request, 'app/productdetail.html',{'product': product})





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

def change_password(request):
 return render(request, 'app/changepassword.html')

def mobile(request):
 return render(request, 'app/mobile.html')

def login(request):
 return render(request, 'app/login.html')

# def customerregistration(request):
#  return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
    def get(self, request):
        form = CustomerRegistrationForm()
        return render(request, 'app/customerregistration.html',{'form': form})
    def post(self, request):
        form=CustomerRegistrationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congratulation!! Registration successful')
            form.save()
        return render(request, 'app/customerregistration.html',{'form': form})


def checkout(request):
 return render(request, 'app/checkout.html')
