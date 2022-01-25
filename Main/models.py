import os 
from django.db import models
from mimetypes import guess_type
from os.path import splitext
# Create your models here.

class Zetechteam(models.Model):
	Name =models.CharField(max_length=100)
	Bio =models.TextField()
	Video=models.FileField(null=True,blank=True,upload_to='Home_page_Video/')
	Photo=models.ImageField(null=True,blank=True,upload_to='Home_page_photo/')
	date_created=models.DateTimeField(auto_now_add=True)
	class Meta:
		ordering=['-date_created']

	def __str__(self):
		return self.Name

	#def Photo_Video(self):
		#type_tuple=guess_type(self.Photo_Video.url)
		#if(type_tuple[0]).__contains__("image"):
			#return "image"
		#elif (type_tuple[0]).__contains__("video"):
			#return "video"

    
class Page(models.Model):
	title=models.CharField(max_length=200)
	sub_title=models.CharField(max_length=2000)
	image=models.ImageField(upload_to='Home_page_photo/',blank=False,null=False) 

