from django.db import models
from Users.models import User
from django.db.models.signals import post_save

class Student(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    date_created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

