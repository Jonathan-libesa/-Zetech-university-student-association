from django.urls import path
from.import views
#from.views import add_post
urlpatterns = [
    #path('add post/',add_post.as_view(),name="add_post"),
    path('news and annoucements',views.new_view_user,name="news_user"),
    ]