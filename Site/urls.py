from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('Alumni.urls')),
    path('',include('Users.urls')),
    path('',include('Main.urls')),
    path('',include('Club.urls')),
    path('',include('Post.urls')),
    path('',include('News.urls')),
    path('',include('Leaders.urls')),
    path('',include('About.urls')),
    path('',include('Zusa_admin.urls')),
    
]
urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

handler404="Main.views.handle_not_found"
handler500="Main.views.handle_server_error"