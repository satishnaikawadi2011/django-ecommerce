from django.urls import path
from  .views import home,register,login

urlpatterns = [
    path('',home.index,name='homePage'),
    path('register',register.Register.as_view(),name='register'),
    path('login',login.Login.as_view(),name='login')
]
