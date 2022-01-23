from django.db import models

# Create your models here.
class About(models.Model):
	title=models.CharField(max_length=250)
	content=models.TextField()
	file=models.FileField(blank=True,null=True,upload_to='About_files/')

	def __str__(self):
		return self.title
