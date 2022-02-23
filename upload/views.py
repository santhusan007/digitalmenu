from django.shortcuts import render
from matplotlib.pyplot import title
from .forms import UploadModelform
from.models import UploadFile
from django.core.files import File
import csv
import boto3
import pandas as pd
from django.conf import settings
from menucard.models import Category,Item
from django.contrib.auth.models import User

AWS_ACCESS_KEY_ID=settings.AWS_ACCESS_KEY_ID
AWS_SECRET_ACCESS_KEY=settings.AWS_SECRET_ACCESS_KEY
AWS_STORAGE_BUCKET_NAME=settings.AWS_STORAGE_BUCKET_NAME

AWS_STORAGE_BUCKET_NAME=settings.AWS_STORAGE_BUCKET_NAME



# Create your views here.

def upload_file_view(request):
    form=UploadModelform(request.POST or None,request.FILES or None)

    client = boto3.client('s3', aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY)
    bucket_name = AWS_STORAGE_BUCKET_NAME
    

    if form.is_valid():
        form.save()
        form=UploadModelform()
        obj=UploadFile.objects.get(activated=False)
        filename=obj.file_name.name

        object_key=filename
        csv_obj = client.get_object(Bucket=bucket_name, Key=object_key)
        csvcontent = csv_obj['Body'].read().decode('utf-8').splitlines()
        lines = csv.reader(csvcontent)
        headers = next(lines)
        print('headers: %s' %(headers))
        for line in enumerate(lines):
            title=line[1][0].upper()
            categories=Category.objects.get(id=line[1][4])
            created_by=User.objects.get(id=line[1][6])
            Item.objects.create(title=title,description=line[1][1],price=line[1][2],type=line[1][3],
                                   categories=categories,label=line[1][5] ,created_by=created_by)
            

        obj.activated=True
        obj.save()
        
        
    

    context={'form':form}
    return render(request,'upload/files.html',context)
