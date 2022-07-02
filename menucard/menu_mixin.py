from menucard.models import Category
from django.db.models import Count,Q,F


class MainView:
    """ class to filter the item based on non veg and veg items using the contains and 
    exclude fucntion of django ORM """
    def __init__(self,check1,check2,check3):
        
        self.check1=check1 # checking the hotel id of the category forign key and hotel id
        self.check2=check2 # check for the category is active or not
        self.check3=check3 # check for the item is active or not

    
    def cuisine(self,types):
        """ filter the cuisine with types veg or non veg as arguments"""
        details=(
            Category.objects.filter(Q(Category__type__startswith=types) & self.check1 & self.check2 & self.check3)
            .prefetch_related('Category').annotate(items_count=Count('Category'))
            #.annotate(cattype=F('Category__type'))
            .order_by('id')
                ) 
        return details
   
      
    def allitem(self):
        details=(
            Category.objects.filter(self.check1 & self.check2 & self.check3)
            .prefetch_related('Category').annotate(items_count=Count('Category'))
            .order_by('id')  
            )
        
        return details
