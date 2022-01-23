from django.contrib import admin
from.models import*
# Register your models here.
class PostAdmin(admin.ModelAdmin):
	list_display=('Title','slug','created_on')
	search_fields=['Title','content']
	#prepopulated_fields={'slug':('Title',)}
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)
admin.site.register(Category)
