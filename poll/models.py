from django.db import models
from Users.models import User
from django.core.exceptions import ValidationError
# Create your models here.

STATUS = (
    (0,"Draft"),
    (1,"Publish")

 )
class Electiontype(models.Model):
	Election_Title=models.CharField(max_length=250)
	status =models.IntegerField(choices=STATUS,default=0)

	def __str__(self):
		return self.Election_Title

	 



class positions(models.Model):
	Name=models.CharField(max_length=200)
	status =models.IntegerField(choices=STATUS,default=0)

	def __str__(self):
		return self.Name




class candidate(models.Model):
	reg_no=models.CharField(max_length=50)
	first_name=models.CharField(max_length=30)
	last_name=models.CharField(max_length=30)
	position=models.ForeignKey(positions,on_delete=models.SET_NULL,null=True,blank=False)
	Photo=models.ImageField(null=False,blank=False,upload_to='Polls_Video/')
	total_votes = models.IntegerField(default=0, editable=False)

	class Meta:
		ordering=['-total_votes']
		
	def __str__(self):
		return self.first_name

class ControlVote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    position = models.ForeignKey(positions, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

    def __str__(self):
        return "{} - {} - {}".format(self.user, self.position, self.status)
