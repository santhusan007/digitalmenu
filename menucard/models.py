from django.db import models
#from django.conf import settings
from django.shortcuts import reverse
#from django.utils import timezone
from django.contrib.auth.models import User
#from PIL import Image

# Create your models here.

class Hotel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,blank=True)
    name= models.CharField(max_length=100,blank=True)
    header=models.CharField(max_length=50,blank=True)
    address=models.CharField(max_length=250,blank=True)
    bgcolor= models.CharField(max_length=100,blank=True)
    mobile=models.CharField(max_length=100,blank=True)
    whatsapplink=models.CharField(max_length=100,blank=True)
    mycolor= models.CharField(max_length=100,blank=True)
    catcolor=models.CharField(max_length=100,blank=True)
    bordercolor=models.CharField(max_length=100,blank=True)
    specialheading=models.CharField(max_length=250,blank=True)
    bgimage = models.ImageField(upload_to='images/',blank=True,null=True)
    pureveg=models.BooleanField(default=True)
    message1=models.CharField(max_length=250,blank=True)
    message2=models.CharField(max_length=250,blank=True)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    title = models.CharField(max_length=225)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,blank=True)
    active=models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Categories"
       

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})

    @property
    def get_products(self):
     return Item.objects.filter(categories__title=self.title)

class Item(models.Model):

    TYPE=(
        
        ('VEG','VEG'),
        ('NON-VEG','NON-VEG'),
        
        )
    LABELS = (
        ('Recommended', 'Recommended'),
        ('Special', 'Special'),
        ('Offer', 'Offer'),
    )   
    
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=250,blank=True)
    price = models.CharField(max_length=250,blank=True)
    image = models.ImageField(upload_to='images/',blank=True,null=True)
    type= models.CharField(max_length=25, choices=TYPE, blank=True)
    categories = models.ForeignKey(Category, related_name='Category', blank=True, on_delete=models.CASCADE)
    label = models.CharField(max_length=15, choices=LABELS, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel=models.ForeignKey(Hotel,on_delete=models.CASCADE,blank=True)
    active=models.BooleanField(default=True,blank=False)
    

    def __str__(self):
        return self.title
       

    @property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

   
    

   


