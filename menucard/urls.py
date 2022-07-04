from django.contrib import admin
from django.urls import path
from .views import ( newMenuDisplay,landing,newMenuVegDisplay,newMenuNonVegDisplay,hotellist,newMenuDisplayJson)



app_name = "menucard"
urlpatterns = [
    
    path('',landing , name='landing'),   
    path('itemlist/',hotellist , name='hotellist'), 
    path('json/<str:header>',newMenuDisplayJson , name='itemjson'), 
    path('<str:header>/',newMenuDisplay , name='mymenu'),
    path('veg/<str:header>/',newMenuVegDisplay , name='mymenuveg'),
    path('nonveg/<str:header>/',newMenuNonVegDisplay , name='mymenunonveg'),
    
   
    
]
