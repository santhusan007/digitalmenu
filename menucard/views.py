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
from django.db.models import Count,Q
from django.views.decorators.cache import cache_page

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

#@cache_page(60*10080)
def newMenuDisplay(request,header):    
    hotel=Hotel.objects.get(header=header)
    id=hotel.id
    name= hotel.name
    header=hotel.header
    address=hotel.address
    bgcolor= hotel.bgcolor
    mycolor= hotel.mycolor
    catcolor=hotel.catcolor
    bordercolor=hotel.bordercolor
    bgimage=hotel.bgimage
    mobile=hotel.mobile
    whatsapplink=hotel.whatsapplink
    message1=hotel.message1
    message2=hotel.message2    
    check1 = Q(created_by_id=id)
    check2=Q(active=True)
    check3=Q(Category__active=True)        
    pureveg=hotel.pureveg
    # if request.method=='POST':
    #     type=request.POST.get("type")

    #     if type == "VEG":  
    #         details=Category.objects.filter(check1 & check2 & check3)\
    #         .exclude(Q(Category__type__contains='NON'))\
    #         .prefetch_related('Category').annotate(items_count=Count('Category'))\
    #         .order_by('id')

    #     elif type == "NON-VEG":
    #         details=Category.objects.filter(check1 & check2 & check3)\
    #         .exclude(Q(Category__type__startswith='VEG'))\
    #         .prefetch_related('Category').annotate(items_count=Count('Category'))\
    #         .order_by('id')

    #     else :
    #         details=Category.objects.filter(check1 & check2 & check3)\
    #         .prefetch_related('Category').annotate(items_count=Count('Category'))\
    #         .order_by('id')
        
        # context= {
            
        #     "hotel":hotel,"details":details,"name": name,"header":header,
        #     "address":address,"bgcolor": bgcolor,"mycolor": mycolor,
        #     "catcolor":catcolor,"bordercolor":bordercolor,
        #     "bgimage":bgimage,"mobile":mobile,"whatsapplink":whatsapplink,
        #     "message1":message1,"message2":message2,"pureveg":pureveg,
        #     }
        # return render(request, 'menucard/newmenu.html', context)

    
    
    details=Category.objects.filter(check1 & check2 & check3)\
        .prefetch_related('Category').annotate(items_count=Count('Category'))\
        .order_by('id')
    context= {
            
        "hotel":hotel,"details":details,"name": name,"header":header,
            "address":address,"bgcolor": bgcolor,"mycolor": mycolor,
            "catcolor":catcolor,"bordercolor":bordercolor,
            "bgimage":bgimage,"mobile":mobile,"whatsapplink":whatsapplink,
            "message1":message1,"message2":message2,"pureveg":pureveg,
            }

    return render(request, 'menucard/newmenu.html', context)
   
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
        # hotels=Hotel.objects.get(user=request.user)
        # hotel_id=hotels.id
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