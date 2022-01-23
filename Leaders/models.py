from django.db import models
from Users.models import User
# Create your models here.

class categerioes(models.Model):
	name=models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Leader(models.Model):
	leader_Name=models.CharField(max_length=250)
	leader_Reg_number=models.CharField(max_length=250)
	category=models.ForeignKey(categerioes,on_delete=models.SET_NULL,null=True)
	about=models.TextField(null=False)
	image=models.ImageField(null=False,upload_to='Leader_profile_picture/')
	date_created=models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.leader_Name
