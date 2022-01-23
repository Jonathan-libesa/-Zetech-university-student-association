from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.



class User(AbstractUser):
	username=models.CharField(max_length=200,null=True,unique=True)
	email=models.EmailField(unique=True,null=True)
	first_name = models.CharField(max_length=100)
	last_name=models.CharField(max_length=100)
	phone=models.CharField(max_length=150,null=True,blank=True)
	profile_pic=models.ImageField(default="no_avatar.jpg",null=True,blank=False,upload_to='User_profile_picture/')
	Website=models.URLField(null=True,blank=True)
	Bio=models.TextField(null=True,blank=True)
	is_alumni=models.BooleanField(default=False)
	is_student=models.BooleanField(default=False)
	is_email_verified = models.BooleanField(default=False)

	USERNAME_FIELD='username'
	REQUIRED_FIELDS=['email']
 
