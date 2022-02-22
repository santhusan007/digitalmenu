from django.contrib import admin
from django.urls import path
from .views import ( MenuListView,ItemCreateView,menuDetail,item_list,
                        ItemDeleteView,ItemUpdateView,landing)



app_name = "menucard"
urlpatterns = [
    
    path('',landing , name='landing'),
    path('hotel/',MenuListView.as_view() , name='menu'),
    path('item/new/', ItemCreateView.as_view(), name='item-create'),
    path('dishes/<int:id>',menuDetail, name='dishes'),
    path('item-update/<int:pk>/', ItemUpdateView.as_view(), name='item-update'),
    path('item-delete/<int:pk>/', ItemDeleteView.as_view(), name='item-delete'),
    path('item_list/', item_list, name='item_list'),
    
]
