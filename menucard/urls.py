from django.contrib import admin
from django.urls import path
from .views import ( newMenuDisplay,landing,)



app_name = "menucard"
urlpatterns = [
    
    path('',landing , name='landing'),    
    path('<str:header>/',newMenuDisplay , name='mymenu'),
   
    
]
