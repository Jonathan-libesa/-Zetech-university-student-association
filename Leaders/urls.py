from django.urls import path
from.import views
urlpatterns = [
    #path('add post/',add_post.as_view(),name="add_post"),
     path('my/leaderview/',views.leaderview,name="leader-view"),
    ]