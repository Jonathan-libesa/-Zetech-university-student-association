from django.db import models
from Users.models import User
from autoslug import AutoSlugField
from mimetypes import guess_type
# Create your models here.
class Club(models.Model):
	Name=models.CharField(max_length=250)
	slug=AutoSlugField(populate_from ='Name')
	About=models.TextField(null=True,blank=True)
	Chairperson=models.ForeignKey(User,on_delete=models.SET_NULL, null=True,blank=True)
	Parton=models.ForeignKey(User,related_name='Parton',on_delete=models.SET_NULL, null=True,blank=True)
	Contact=models.CharField(max_length=70,default=None)
	profile_pic=models.ImageField(default="no_avatar.jpg",null=False,blank=False,upload_to='Club_profile_picture/')
	participants = models.ManyToManyField(User, related_name='participants', blank=True)
	Meeting_place=models.TextField(null=True,blank=True)
	date_created=models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering=['-date_created']

	def __str__(self):
		return self.Name

class Event(models.Model):
	Name=models.CharField('Event Name',max_length=250)
	manager=models.ForeignKey(User,on_delete= models.SET_NULL,blank=False,null=True,related_name='Event_manager')
	date_created=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)
	Venue=models.CharField(max_length=250,blank=False,null=False)
	Club_Name=models.ForeignKey( Club ,on_delete= models.SET_NULL,blank=False,null=True)
	Photo_Video =models.FileField( upload_to='Club_event_file/',null=True,blank=True)
	Description=models.TextField(blank=False)
	

	class Meta:
		ordering=['-updated','-date_created']

	def __str__(self):
		return self.Name

	def Photo_Video_type_html(self):
		type_tuple=guess_type(self.Photo_Video.url,strict=True)
		if(type_tuple[0]).__contains__("image"):
			return "image"
		elif (type_tuple[0]).__contains__("video"):
			return "video"
			

 