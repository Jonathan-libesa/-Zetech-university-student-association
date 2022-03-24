# Generated by Django 3.2.8 on 2022-02-22 16:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Club', '0003_auto_20220125_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='club',
            name='Requirements',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='participants',
            field=models.ManyToManyField(blank=True, default=0, editable=False, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
    ]