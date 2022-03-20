import sys
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Item, Category,Hotel
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.html import mark_safe

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Item)

@admin.register(Hotel)
class HotelAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ['name']
    search_fields = ['name']
    readonly_fields=["image_photo"]

    def image_photo(self, obj):
        return mark_safe('<img src="{url}" width="300" height="200"/>'.format(
            url = obj.bgimage.url,           
            ))

    
    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == "user":
                    # created_by=request.user
                    # if created_by:
                    kwargs["queryset"] = User.objects.filter(username=request.user)
            
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super(HotelAdmin, self).get_fieldsets(request, obj)
        if not request.user.is_superuser:
            return [(None, {'fields': ('name','address','bgimage','image_photo')}),]
        else:
            return fieldsets   


       

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ['title']
    search_fields = ['title']
    # readonly_fields = ["created_by"]
    list_per_page = sys.maxsize

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser:
                return qs
            return qs.filter(created_by=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == "created_by":
                    # created_by=request.user
                    # if created_by:
                created_by=User.objects.all()
                if not request.user.is_superuser:
                        kwargs["queryset"] = User.objects.filter(username=request.user)
                else:
                        kwargs["queryset"] = created_by

            elif db_field.name == "hotel" :
                hotel=Hotel.objects.all()   
                if not request.user.is_superuser:
                    kwargs["queryset"] = Hotel.objects.filter(user=request.user)
                else:
                     kwargs["queryset"]=hotel
    
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
            
            
            return super().formfield_for_foreignkey(db_field, request, **kwargs)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    view_on_site = False
    search_fields = ['title']
    list_filter = ('label',('categories',admin.RelatedOnlyFieldListFilter))
    # readonly_fields= ["created_by"]
    list_per_page = sys.maxsize
    readonly_fields=["image_photo"]
    list_display = ['title','description','price']

    # def image_tag(self, obj):
    #     return format_html('<img src="{}" width="200" height="100" />'.format(obj.image.url))
    # image_tag.short_description = 'Image'
  
    def image_photo(self, obj):
        return mark_safe('<img src="{url}" width="200" height="200"/>'.format(
            url = obj.image.url,           
            ))
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(created_by=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        
            if db_field.name == "created_by":
                created_by=User.objects.all()

                if not request.user.is_superuser:
                    kwargs["queryset"] = User.objects.filter(username=request.user)
                else:
                     kwargs["queryset"] = created_by
            
            elif db_field.name == "categories":
                categories=Category.objects.all()
                if not request.user.is_superuser:
                    kwargs["queryset"] = Category.objects.filter(created_by=request.user)
                else:
                     kwargs["queryset"]=categories

            elif db_field.name == "hotel" :
                hotel=Hotel.objects.all()   
                if not request.user.is_superuser:
                    kwargs["queryset"] = Hotel.objects.filter(user=request.user)
                else:
                     kwargs["queryset"]=hotel
    
            return super().formfield_for_foreignkey(db_field, request, **kwargs)


# changing the admin site headder
admin.site.index_title = "Menu Details"
admin.site.site_header = "My Digital Menu"
admin.site.site_title = "My Digital Menu"
