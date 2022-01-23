from django.db import models
from Users.models import User
from datetime import datetime,time
from ckeditor.fields import RichTextField
from django.urls import reverse
# Create your models here.
class Announcement(models.Model):
	Author=models.ForeignKey(User,null=True,on_delete= models.CASCADE)
	image=models.ImageField(null=True,blank=True,upload_to='News_images/')
	Subject=models.CharField(max_length=255)
	body=RichTextField(blank=True,null=True)
	files=models.FileField( blank=True,null=True,upload_to='News_files/')
	created_on=models.DateTimeField(auto_now_add=True)
	updated=models.DateTimeField(auto_now=True)

	class Meta:
		ordering=['-created_on']
	def __str__(self):
		return self.Subject+ '|' +str(self.Author)
	def get_absolute_url(self):
		#return reverse('details',args=(str(self.id)))
		return reverse('news')
