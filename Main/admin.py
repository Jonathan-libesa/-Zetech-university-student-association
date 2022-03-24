from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import*
# Register your models here.


class YoutubeAdmin(AdminVideoMixin, admin.ModelAdmin):
    pass

admin.site.register(Youtube, YoutubeAdmin)