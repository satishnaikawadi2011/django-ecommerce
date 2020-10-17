from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password,check_password
from ..models.product import Product
from ..models.category import Category
from .. models.customer import Customer
from django.views import View
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





    
