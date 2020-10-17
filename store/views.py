from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
# Create your views here.
# def index(request):
#     return HttpResponse('<h1>My Store App</h1>')

def index(request):
    products = None
    categories = Category.get_all_categories()
    categoryId = request.GET.get('category')
    if categoryId:
        products = Product.get_products_by_category(categoryId)
    else:
        products = Product.get_all_products();
    data = {}
    data['products'] = products
    data['categories'] = categories
    return render(request,'index.html',data)


def validateRegister(customer):
        error_message = None
        if not customer.first_name:
            error_message = "First name is required !"
        elif not customer.last_name:
            error_message = "Last name is required !"
        elif not customer.password:
            error_message = "Password is required !"
        elif len(customer.password)<6:
            error_message = "Password must be at least 6 characters long!"
        elif not customer.phone:
            error_message = "Phone number is required !"
        elif len(customer.phone) is not 10:
            error_message = "Enter a valid phone number!"
        elif customer.isExists():
            error_message = "Email address is already registered , login instead!"
        return error_message

def registerUser(request):
        data = request.POST
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        email = data.get('email')
        password = data.get('password')
        phone = data.get('phone')

        customer = Customer(first_name=first_name,last_name=last_name,email=email,password=password,phone=phone)
        error_message = validateRegister(customer)
        values = {'first_name':first_name,'last_name':last_name,'email':email,'phone':phone}

        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect('homePage')
        else:
            data = {'error':error_message,'values':values}
            return render(request,'register.html',data)

def register(request):
    if request.method == 'GET':
        return render(request,'register.html')
    else:
        return registerUser(request)

def login(request):
    return render(request,'login.html')