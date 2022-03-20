from typing import Counter
from django.shortcuts import render,redirect
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import  ListView,CreateView,UpdateView,DeleteView
from .models import Item,Category,Hotel
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.db.models import Count

# Create your views here.

def landing(request):    
    return render(request, 'menucard/landing.html')

def menuDetail(request,id):
    item = Item.objects.filter(id=id).first()
    
    context = {
        'item' : item,        
    }
    return render(request, 'menucard/dishes.html', context)

class MenuListView(ListView):
    model = Category
    template_name = 'menucard/home.html'
    context_object_name = 'menu_items'


def newMenuDisplay(request,header):
    
    hotel=Hotel.objects.get(header=header)
    id=hotel.id
    name= hotel.name
    header=hotel.header
    address=hotel.address
    bgcolor= hotel.bgcolor
    mycolor= hotel.mycolor
    catcolor=hotel.catcolor
    bgimage=hotel.bgimage
    details=Category.objects.filter(created_by_id=id).prefetch_related('Category').annotate(items_count=Count('Category')).order_by('id')
    
    context= {
        
        "hotel":hotel,
        "details":details ,
         "name": name,
        "header":header,
        "address":address,
        "bgcolor": bgcolor,
        "mycolor": mycolor,
        "catcolor":catcolor,
        "bgimage":bgimage
        }
    print(bgcolor,mycolor,catcolor)

    return render(request, 'menucard/newmenu.html', context)
    
    
    
    
class GlobalListView(ListView):
    pass
    # model = Category
    # template_name = 'menucard/globalbinge.html'
    # #context_object_name = 'menu_items'
    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     #context['details']=Category.objects.filter(created_by_id=2).annotate(items_count=Count('Category')).order_by('id')
    #     context['details']=Category.objects.filter(created_by_id=2)\
    #                         .prefetch_related('Category')\
    #                         .annotate(items_count=Count('Category'))\
    #                         .order_by('id')
    #     return context

class TheBunkerListView(ListView):
    pass
    # model = Category
    # template_name = 'menucard/thebunker.html'
    # #context_object_name = 'menu_items'
    # def get_context_data(self, **kwargs):
    #     context= super().get_context_data(**kwargs)
    #     #context['bunker']=Category.objects.filter(created_by_id=3).annotate(items_count=Count('Category')).order_by('id')
    #    #optimized the query using prefetch related funtion
    #     context['details']=Category.objects.filter(created_by_id=3)\
    #                         .prefetch_related('Category')\
    #                         .annotate(items_count=Count('Category'))\
    #                         .order_by('id')\

    #     return context    

class ItemCreateView(LoginRequiredMixin, CreateView):
    model = Item
    fields = ['title', 'image', 'description', 'price','type','categories', 'label']
        
    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Item
    fields = ['title', 'image', 'description', 'price', 'label']

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return False

class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Item
    success_url = '/item_list'

    def test_func(self):
        item = self.get_object()
        if self.request.user == item.created_by:
            return True
        return False

def item_list(request):
    if not request.user.is_authenticated:
            # Redirect them to the home page if not 
            return redirect('menucard:landing')
    else:
        items = Item.objects.filter(created_by=request.user)
        context = {
            'items':items
                    }
    return render(request, 'menucard/item_list.html', context)

def error_404(request,exception=None):
        data = {}
        return render(request,'menucard/error_404.html', data)

def error_500(request,exception=None):
        data = {}
        return render(request,'menucard/error_500.html', data)