from django.urls import path
from.import views

urlpatterns = [
    path('alumni/',views.homepage,name='alumni'),
    path('alumni_list/',views.alumnilist,name='list'),
    path('joblist/',views.Job,name="job_list"),
    path('job_view/<str:pk>',views.job_view,name="job_view"),
    path('forum_list/',views.forum_create_list,name="forum"),
    #path('create-forum/', views.createforum, name="create-forum"),
    #path('update-forum/<str:pk>/',views.updateForum, name="update-forum"),
    #path('forum_details/<str:pk>/', views.forum, name="forum-details"),
    path('delete/<str:pk>/', views.delete, name='delete-forum'),
    #path('job/create/', views.job_create, name='job_create'),
    ]