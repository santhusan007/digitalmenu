from django import forms
from .models import UploadFile

class UploadModelform(forms.ModelForm):
    class Meta:
        model=UploadFile
        fields=('file_name',)