from django.contrib import admin
from django.urls import path
from .views import ( newMenuDisplay,landing,newMenuVegDisplay,newMenuNonVegDisplay,)



app_name = "menucard"
urlpatterns = [
    
    path('',landing , name='landing'),    
    path('<str:header>/',newMenuDisplay , name='mymenu'),
    path('veg/<str:header>/',newMenuVegDisplay , name='mymenuveg'),
    path('nonveg/<str:header>/',newMenuNonVegDisplay , name='mymenunonveg'),
   
    
]
