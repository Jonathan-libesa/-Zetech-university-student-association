from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(Alumni)
admin.site.register(Career)
admin.site.register(Event)
admin.site.register(Forum)
admin.site.register(Comment)