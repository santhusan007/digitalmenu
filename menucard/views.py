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
def newMenuDisplay(request,header):    
    hotel=Hotel.objects.get(header=header)
    check1=Q(hotel_id=hotel.id)
    check2=Q(active=True)
    check3=Q(Category__active=True)   
    #filtering base on veg non veg and all  
    menu=MainView(check1,check2,check3)
    
    details=menu.allitem()        
    context= {"hotel":hotel,"details":details,}
    return render(request, 'menucard/newmenu.html', context)

def newMenuVegDisplay(request,header):    
    hotel=Hotel.objects.get(header=header)
    check1=Q(hotel_id=hotel.id)
    check2=Q(active=True)
    check3=Q(Category__active=True)   
    #filtering base on veg non veg and all  
    menu=MainView(check1,check2,check3)    
    details=menu.cuisine("VEG")        
    context= {"hotel":hotel,"details":details,}
    return render(request, 'menucard/newmenuveg.html', context)

def newMenuNonVegDisplay(request,header):    
    hotel=Hotel.objects.get(header=header)
    check1=Q(hotel_id=hotel.id)
    check2=Q(active=True)
    check3=Q(Category__active=True)   
    #filtering base on veg non veg and all  
    menu=MainView(check1,check2,check3)    
    details=menu.cuisine("NON-VEG")        
    context= {"hotel":hotel,"details":details,}
    return render(request, 'menucard/newmenunonveg.html', context)
       
 
def error_404(request,exception=None):
        data = {}
        return render(request,'menucard/error_404.html', data)

def error_500(request,exception=None):
        data = {}
        return render(request,'menucard/error_500.html', data)

def hotellist(request):
    item=Item.objects.all().values()
    item=list(item)
    data=dumps(item)
    cat=Category.objects.all().values()
    cat=list(cat)
    catdata=dumps(cat)
    return render(request, "menucard/testhotel.html", {"data": data, "catdata":catdata})



def newMenuDisplayJson(request,header):    
    hotel=Hotel.objects.get(header=header)
    check1=Q(hotel_id=hotel.id)
    check2=Q(active=True)
    check3=Q(Category__active=True)   
    #filtering base on veg non veg and all  
    menu=MainView(check1,check2,check3)
    
    cat=menu.allitem().values()        
    cat=list(cat)
    finalcat=dumps(cat)  

    items=Item.objects.all().filter(hotel_id=hotel.id).values() 
    items=list(items)
    finalitem=dumps(items)


    context= {"hotel":hotel,"cat":finalcat,"item":finalitem}
    return render(request, 'menucard/newmenuJson.html', context)

