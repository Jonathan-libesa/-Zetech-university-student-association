from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.db import transaction
from .models import User
from Student.models import Student
from Alumni.models import Alumni
from django.forms import ModelForm
from Post.models import *
from Main.validators import validate_file_size,file_size

class StudentSignUpForm(UserCreationForm):
    first_name=forms.CharField(required=True)
    last_name=forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model=User
        fields=['username','first_name','last_name','email','password1','password2']
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        student = Student.objects.create(user=user)
        student.save()
        return user

class AlumniSignUpForm(UserCreationForm):
    first_name = forms.CharField(required=True)
    last_name = forms.CharField(required=True)
    class Meta(UserCreationForm.Meta):
        model = User
        fields=['username','first_name','last_name','email','password1','password2']

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_alumni = True
        user.first_name = self.cleaned_data.get('first_name')
        user.last_name = self.cleaned_data.get('last_name')
        user.save()
        alumni = Alumni.objects.create(user=user)
        alumni.save()
        return user

class UserForm(ModelForm):
    profile_pic=forms.ImageField(required=True,validators=[file_size])
    class Meta:
        model = User
        fields = ['username', 'email','first_name','last_name','phone','profile_pic','Website','Bio']


class postForm(forms.ModelForm):
    Photo= forms.FileField(required=False, validators=[validate_file_size])
    class Meta:
        model = Post
        fields ='__all__'
        exclude =['author']
