from menucard.models import Hotel
from rest_framework import serializers


class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model=Hotel
        fields=['name','address']



