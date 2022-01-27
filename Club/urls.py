from django.urls import path
from.import views
#from.views import 

urlpatterns = [
    path('club_list/',views.clubs,name="clubuser"),
    path('club/<str:pk>/participants/remove',views.removeparticipants,name="remove_follower"),
    path('club/<str:pk>/participants/add',views.addparticipants,name="add_followers"),
    path('club_details/<str:pk>',views.Club_details,name="details"),
    path('Club_event/<str:club>',views.Club_event,name="Clubevent"),
    path('updateclub/<str:pk>',views. Editclub,name="editclub"),
    path('createEvent/<str:pk>',views.createEvent,name="Add-event"),
    path('updateevent/<str:pk>',views.EditEvent,name="edit-event"),
    path('participants_club_users/<str:pk>',views.groupfollower,name="followers"),
    path('Delete-Event/<str:pk>',views.DeleteEvent,name="delete-event"),
    #path('load-more-data',views.load_more_data,name='load_more_data'),
    #path('load-more',views.load_more,name='load-more'),
    ]