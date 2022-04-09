from .models import Category
from django.db.models import Count,Q


class MainView:

    def __init__(self,check1,check2,check3):
        
        self.check1=check1
        self.check2=check2
        self.check3=check3

    def veg(self):
        
        details=Category.objects.filter(self.check1 & self.check2 & self.check3)\
                .exclude(Q(Category__type__contains='NON'))\
                .prefetch_related('Category').annotate(items_count=Count('Category'))\
                .order_by('id') 
        return details
        
    def nonveg(self):
               
        details=Category.objects.filter(self.check1 & self.check2 & self.check3)\
            .exclude(Q(Category__type__startswith='VEG'))\
            .prefetch_related('Category').annotate(items_count=Count('Category'))\
            .order_by('id')
        return details
        
    def allitem(self):
        details=Category.objects.filter(self.check1 & self.check2 & self.check3)\
            .prefetch_related('Category').annotate(items_count=Count('Category'))\
            .order_by('id')  
        
        return details

# function for getting the image in admin site

    

