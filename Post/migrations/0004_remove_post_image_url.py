# Generated by Django 3.2.8 on 2022-01-25 08:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0003_auto_20220125_1042'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='image_url',
        ),
    ]
