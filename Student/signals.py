from Alumni.models import Alumni
from Student.models import Student
from User.models import User
from django.db.models.signals import post_save
from django.contrib.auth.models import Group


def create_user_profile(sender, instance, request, **kwargs):
    if request.user.is_staff:
        staff(user=instance, profile='staff').save()
    elif request.user.is_alumni:
        Alumni(user=instance,profile='Alumni').save()
    else:
        Student(user=instance, profile='Student').save()