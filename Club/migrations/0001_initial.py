# Generated by Django 3.2.8 on 2022-05-16 21:46

import autoslug.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='Name')),
                ('About', models.TextField(blank=True, null=True)),
                ('Contact', models.CharField(default=None, max_length=70)),
                ('profile_pic', models.ImageField(default='no_avatar.jpg', upload_to='Club_profile_picture/')),
                ('Meeting_place', models.TextField(blank=True, null=True)),
                ('Requirements', models.TextField(blank=True, null=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('Chairperson', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('Parton', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Parton', to=settings.AUTH_USER_MODEL)),
                ('participants', models.ManyToManyField(blank=True, default=0, editable=False, related_name='participants', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_created'],
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=250, verbose_name='Event Name')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('Venue', models.CharField(max_length=250)),
                ('Photo', models.ImageField(blank=True, null=True, upload_to='Club_event_file/')),
                ('Description', models.TextField()),
                ('Club_Name', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='Club.club')),
                ('manager', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Event_manager', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-updated', '-date_created'],
            },
        ),
    ]
