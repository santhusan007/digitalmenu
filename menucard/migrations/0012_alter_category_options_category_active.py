# Generated by Django 4.0.2 on 2022-03-21 05:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0011_item_active'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'Categories'},
        ),
        migrations.AddField(
            model_name='category',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]