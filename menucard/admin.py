from django.contrib import admin
from .models import Item,Category

# Register your models here.

#admin.site.register(Category) 
#admin.site.register(Item) 

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
   list_display=['title','created_by']

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
   list_display=['title','description','price','created_by']