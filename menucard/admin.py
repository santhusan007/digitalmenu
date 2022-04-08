import sys
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Item, Category,Hotel
from django.contrib.auth.models import User
from django.utils.html import format_html
from django.utils.html import mark_safe

# Register your models here.
# admin.site.register(Category)
# admin.site.register(Item)

def is_admingroup(user):
     return user.groups.filter(name='admingroup').exists()
#ImportExportModelAdmin
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
            if request.user.is_superuser or is_admingroup(request.user)  :
                return qs
            return qs.filter(user=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name == "user":
                created_by=User.objects.all()
                if  request.user.is_superuser or is_admingroup(request.user) :
                    kwargs["queryset"] = created_by                
                else:
                    kwargs["queryset"] = User.objects.filter(username=request.user)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
    
    def get_fieldsets(self, request, obj=None):
        fieldsets = super(HotelAdmin, self).get_fieldsets(request, obj)
        if request.user.is_superuser or is_admingroup(request.user):
            return fieldsets             
        return [(None, {'fields': ('name','address','bgimage','image_photo')}),]
              
#ImportExportModelAdmin,
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    view_on_site = False
    list_display = ['title','active']
    search_fields = ['title']
    # readonly_fields = ["created_by"]
    list_per_page = sys.maxsize
    ordering=('id',)
    list_editable = ('active',)

    def get_queryset(self, request):
            qs = super().get_queryset(request)
            if request.user.is_superuser :
                return qs
            return qs.filter(created_by=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name in ["created_by","hotel" ]:
                    # created_by=request.user
                    # if created_by:
                created_by=User.objects.all()
                if request.user.is_superuser :
                     kwargs["queryset"] = created_by   
                else:
                    kwargs["queryset"] = User.objects.filter(username=request.user)
            return super().formfield_for_foreignkey(db_field, request, **kwargs)
#ImportExportModelAdmin,           
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    view_on_site = False
    search_fields = ['title']
    list_filter = ('label',('categories',admin.RelatedOnlyFieldListFilter))
    # readonly_fields= ["created_by"]
    list_per_page = sys.maxsize
    readonly_fields=["image_photo"]
    list_display = ['title','description','active','price']
    list_editable = ('active',)
    ordering = ('id', )
         
    def image_photo(self, obj):
        return mark_safe('<img src="{url}" width="200" height="200"/>'.format(
            url = obj.image.url,           
            ))
    
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser :
            return qs
        return qs.filter(created_by=request.user)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
            if db_field.name in ["created_by","categories","hotel"]:
                created_by=User.objects.all()
                if  request.user.is_superuser :
                    kwargs["queryset"] = created_by                    
                else:
                    kwargs["queryset"] = User.objects.filter(username=request.user)
            
            return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.index_title = "Menu Details"
admin.site.site_header = "My Digital Menu"
admin.site.site_title = "My Digital Menu"
