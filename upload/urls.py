from django.urls import path 
from .views import upload_file_view

app_name='upload'

urlpatterns = [
    path ('file',upload_file_view,name='upload-view')
]
