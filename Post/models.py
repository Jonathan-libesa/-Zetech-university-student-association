from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from autoslug import AutoSlugField
from datetime import datetime,date
from Users.models import User
from hitcount.models import HitCount
from django.contrib.contenttypes.fields import GenericRelation
from django.shortcuts import render,redirect,reverse
from mimetypes import guess_type
#from urlparse import urlparse
# Create your models here.

class Category(models.Model):
	title=models.CharField(max_length=90)
	title_slug=AutoSlugField(populate_from='title')


	def __str__(self):
		return self.title



class Post(models.Model):
	Title=models.CharField(max_length=200)
	author=models.ForeignKey(User,on_delete= models.CASCADE,related_name='blog_post')
	slug=AutoSlugField(populate_from ='Title')
	updated=models.DateTimeField(auto_now_add=True)
	content=models.TextField(blank=True,null=True)
	created_on=models.DateTimeField(auto_now_add=True)
	Photo=models.ImageField(null=True,blank=True,upload_to='Post_Video/')
	categories=models.ForeignKey(Category,on_delete=models.SET_NULL,null=True,blank=True)
	hit_count_generic = GenericRelation(HitCount,object_id_field='object_pk',related_query_name='hit_count_generic_relation')
	

	class Meta:
		ordering=['-created_on']
	def __str__(self):
		return self.Title


	#def Photo_Video_type_html(self):
		#type_tuple=guess_type(self.Photo_Video.url,strict=True)
		#if(type_tuple[1]).__contains__("image"):
			#return "image"
		#elif (type_tuple[0]).__contains__("video"):
			#return "video"


class Comment(models.Model):
	created_on=models.DateTimeField(auto_now_add=True)
	user=models.ForeignKey(User,on_delete= models.CASCADE,related_name='comment')
	content=models.TextField()
	post=models.ForeignKey('Post',on_delete= models.CASCADE)
	class Meta:
		ordering=['-created_on']
		
	def __str__(self):
		return self.content