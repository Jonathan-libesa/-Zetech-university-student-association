from django import forms
from .models import*
from django.forms import ModelForm
from Main.validators import validate_file_size,file_size
class ClubForm(ModelForm):
	profile_pic=forms.ImageField(required=False, validators=[file_size])
	class Meta:
		model=Club
		fields=['Name','profile_pic','Contact','About','Meeting_place']
		exclude=['Chairperson','Parton','participants']



class EventForm(ModelForm):
	Photo= forms.FileField(required=False, validators=[ validate_file_size])
	class Meta:
		model=Event
		Fields='__all__'
		exclude=['manager','Club_Name']
