# Generated by Django 4.0.2 on 2022-03-20 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0010_category_hotel_item_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
