# Generated by Django 4.0.2 on 2022-03-27 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0017_hotel_pureveg'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='specialheading',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]