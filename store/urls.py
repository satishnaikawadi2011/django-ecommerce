from django.urls import path
from  .views import index,register,login

urlpatterns = [
    path('',index,name='homePage'),
    path('register',register),
    path('login',login)
]
