from django.contrib import admin
from django.urls import path

from .views import ( landing,newMenuDisplayJson)


app_name = "menucard"
urlpatterns = [
    
    path('',landing , name='landing'),   
    path('<str:header>/',newMenuDisplayJson , name='itemjson'), 
        
   
    
]
