from .models import Hotel
from django.db.models import Q
from django.shortcuts import render
from django.views.decorators.cache import cache_page
from menucard.menu_mixin import MainView

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
    if request.method=='POST' :
        types=request.POST.get("type")
        
        if types == "VEG" or types=="NON-VEG":            
            details=menu.cuisine(types)
            
        # elif types == "NON-VEG":
        #     details=menu.cuisine(types)
        else :
            details=menu.allitem()   
        context= {"hotel":hotel,"details":details,"types":types }
        return render(request, 'menucard/newmenu.html', context)
    else:
        details=menu.allitem()        
        context= {"hotel":hotel,"details":details,}
        return render(request, 'menucard/newmenu.html', context)
 
def error_404(request,exception=None):
        data = {}
        return render(request,'menucard/error_404.html', data)

def error_500(request,exception=None):
        data = {}
        return render(request,'menucard/error_500.html', data)
