# Generated by Django 4.0.2 on 2022-02-23 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0004_category_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='price',
            field=models.CharField(blank=True, max_length=250),
        ),
    ]
