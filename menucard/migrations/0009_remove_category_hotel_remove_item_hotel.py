# Generated by Django 4.0.2 on 2022-03-20 06:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0008_hotel_mobile_hotel_whatsapplink'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='hotel',
        ),
        migrations.RemoveField(
            model_name='item',
            name='hotel',
        ),
    ]
