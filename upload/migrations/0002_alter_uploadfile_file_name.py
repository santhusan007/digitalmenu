# Generated by Django 4.0.2 on 2022-02-23 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='file_name',
            field=models.FileField(upload_to='https://s3.console.aws.amazon.com/s3/object/mmd2022?region=ap-south-1&prefix=csvs/'),
        ),
    ]
