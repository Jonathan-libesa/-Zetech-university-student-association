from django.db import models
from Users.models import User
from ckeditor.fields import RichTextField
from django.db.models.signals import post_save
from mimetypes import guess_type


class Alumni(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    date_created=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.user.username

        
class Career(models.Model):
    author=models.ForeignKey(User,on_delete= models.CASCADE,blank=True,null=True)
    company=models.CharField(max_length=80)
    job_title=models.CharField(max_length=100)
    location=models.CharField(max_length=100)
    Description=models.TextField(blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-updated','-date_created']
    def __str__(self):
        return self.company


class Event(models.Model):
    title=models.CharField(max_length=80)
    Photo=models.ImageField(upload_to='Alumni_Event/',null=True,blank=True)
    Video=models.FileField(upload_to='Alumni_Event/',null=True,blank=True)
    Description=models.TextField(null=True,blank=True)
    date_created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-updated','-date_created']
    def __str__(self):
        return self.title

    #def Photo_Video_type_html(self):
        #type_tuple=guess_type(self.Photo_Video.url,strict=True)
        #if(type_tuple[0]).__contains__("image"):
           # return "image"
        #elif(type_tuple[0]).__contains__("video"):
            #return "video"

    
class Forum(models.Model):
    author=models.ForeignKey(User,on_delete= models.CASCADE,blank=True,null=True)
    title=models.CharField(max_length=80)
    Photo=models.ImageField(upload_to='Forum_Files/',null=True,blank=True)
    description=models.TextField(blank=True,null=True)
    date_created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    class Meta:
        ordering=['-updated','-date_created']
    def __str__(self):
        return self.title

    #def Photo_Video_type_html(self):
        #type_tuple=guess_type(self.Photo_Video.url,strict=True)
        #if(type_tuple[0]).__contains__("image"):
           # return "image"
        #elif (type_tuple[0]).__contains__("video"):
            #return "video"

class Comment(models.Model):
    created_on=models.DateTimeField(auto_now_add=True)
    user=models.ForeignKey(User,on_delete= models.CASCADE,related_name='comments')
    content=models.TextField(null=True)
    forum=models.ForeignKey('Forum',on_delete= models.CASCADE)
    updated=models.DateTimeField(auto_now=True)

    class Meta:
        ordering=['-updated','created_on']
