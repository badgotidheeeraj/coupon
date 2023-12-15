from django.urls import path, include
from . import views

urlpatterns = [
        path('profile/', views.profile, name='dashboard'),   
        path('create/', views.create_post, name='create_post'),   
]
