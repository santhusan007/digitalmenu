from .models import Category, Hotel,Item
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from menucard.menu_mixin import MainView
from json import dumps

# Create your views here.

def landing(request):    
    return render(request, 'menucard/landing.html')

# @cache_page(60*60)

def error_404(request,exception=None):
        data = {}
        return render(request,'menucard/error_404.html', data)

def error_500(request,exception=None):
        data = {}
        return render(request,'menucard/error_500.html', data)

def newMenuDisplayJson(request,header):    
    hotel=Hotel.objects.get(header=header)
    check1=Q(hotel_id=hotel.id)
    check2=Q(active=True)
    check3=Q(Category__active=True)   
    #filtering base on veg non veg and all  
    menu=MainView(check1,check2,check3)

    details=menu.allitem() 
     
    image_url={}
    for cat in details:
        for item in cat.Category.all():
            if item.image:
                image_url[item.id]=item.image.url
    
    cat=menu.allitem().values()        
    cat=list(cat)
    finalcat=dumps(cat)  

    items=Item.objects.all().filter(hotel_id=hotel.id).values() 
    items=list(items)
    for i in items:
        for image in image_url:
            if i['id']==image:
                i['image']=image_url[i['id']]
                
     
    finalitem=dumps(items)


    context= {"hotel":hotel,"cat":finalcat,"item":finalitem}
    return render(request, 'menucard/newmenuJson.html', context)

