# Generated by Django 4.0.2 on 2022-03-20 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menucard', '0006_hotel'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='hotel',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='menucard.hotel'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='item',
            name='hotel',
            field=models.ForeignKey(blank=True, default=2, on_delete=django.db.models.deletion.CASCADE, to='menucard.hotel'),
            preserve_default=False,
        ),
    ]
