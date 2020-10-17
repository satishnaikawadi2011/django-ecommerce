from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from ..models.product import Product
from ..models.category import Category
from ..models.customer import Customer
from django.views import View



class Login(View):
    def get(self,request):
        return render(request,'login.html')

    def post(self,request):
        error_message = None
        data = request.POST
        email = data.get('email')
        password = data.get('password')
        customer = Customer.get_cusomer_by_email(email)
        error_message =  self.validateLogin(customer,email,password)
        if not error_message:
            return redirect('homePage')
        else:
            return render(request,'login.html',{'error':error_message,'email':email})

    def validateLogin(self,customer,email,password):
        error_message = None
        if not email:
            error_message = "Email address is required !"
        elif not password:
            error_message = "Password is required !"
        elif not customer:
            error_message = "No customer found with given email address !" 
        elif not check_password(password,customer.password):
            error_message = "Invalid credentials , try again !"
        return error_message