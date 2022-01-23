from django.urls import path
from.import views

urlpatterns = [
    path('',views.home,name="home"),
    #path('home/',views.home,name="home"),
    path('my/',views.user,name="User"),
    #path('add post/',add_post.as_view(),name="add_post"),
    #path('news and annoucements/',views.newsview,name="news"),

    ]