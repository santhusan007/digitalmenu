# Generated by Django 4.0.2 on 2022-02-21 00:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0002_alter_item_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
