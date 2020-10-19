from django.urls import path
from  .views import home,register,login

urlpatterns = [
    path('',home.index,name='homePage'),
    path('register',register.Register.as_view(),name='register'),
    path('login',login.Login.as_view(),name='login'),
    path('add_to_cart',home.add_to_cart,name="add_to_cart"),
    path('increament_cart_quantity',home.increament_cart_quantity,name="increament_cart_quantity"),
    path('decreament_cart_quantity',home.decreament_cart_quantity,name='decreament_cart_quantity')
]
