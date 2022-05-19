from django.forms import ModelForm
from django import forms
from django.db import transaction
from Users.models import*
from Student.models import Student
from Alumni.models import*
from News.models import*
from Club.models import*
from Leaders.models import *
from Post.models import *
from About.models import *
from Main.models import *
from poll.models import*

class userForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','groups','date_joined','last_login','is_alumni','is_student','is_email_verified','is_staff','is_active']


class NewsForm(forms.ModelForm):
    class Meta:
        model=Announcement
        Fields='__all__'
        exclude=['Author']

class clubForm(forms.ModelForm):
    class Meta:
        model=Club
        fields='__all__'
        

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['username','first_name','last_name','email','password','groups','is_alumni','is_student','is_email_verified','is_staff','is_active']
       # fields = '__all__'


class leaderForm(forms.ModelForm):
    class Meta:
        model =Leader
        fields = '__all__'

class PostForm(forms.ModelForm):
    #Photo_Video= forms.FileField(required=False, validators=[validate_file_size])
    class Meta:
        model = Post
        fields ='__all__'
        exclude =['author']

class forumForm(forms.ModelForm):
    class Meta:
        model=Forum
        fields=['title','description']
        exclude=['author']

class catergoriesForm(forms.ModelForm):
    class Meta:
        model=categerioes
        fields='__all__'

        widgets={
        'name':forms.TextInput(attrs={'class':'form-control'}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model=Category
        fields='__all__'

        widgets={
        'title':forms.TextInput(attrs={'class':'form-control'}),
        }


class aboutForm(forms.ModelForm):
    class Meta:
        model=About
        fields='__all__'


class ZetechForm(forms.ModelForm):
    class Meta:
        model=Zetechteam
        fields='__all__'


class pageForm(forms.ModelForm):
    class Meta:
        model=Page
        fields='__all__'



class  positionForm(forms.ModelForm):
    class Meta:
        model= positions
        fields='__all__'

class  candidateForm(forms.ModelForm):
    class Meta:
        model= candidate
        fields='__all__'