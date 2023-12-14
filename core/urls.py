from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.userLogin, name='userLogin'),
    path('register/', views.userRegister, name='userRegister'),
    path('logout/', views.userLogout, name='userLogout'),
]
