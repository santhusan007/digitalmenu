from django.shortcuts import render,redirect
from django.conf import settings
from django.shortcuts import reverse
from django.utils import timezone
from django.contrib.auth.models import User
from django.views.generic import  ListView,CreateView,UpdateView,DeleteView
from .models import Item,Category
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required

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

class GlobalListView(ListView):
    model = Category
    template_name = 'menucard/globalbinge.html'
    context_object_name = 'menu_items'

    

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

