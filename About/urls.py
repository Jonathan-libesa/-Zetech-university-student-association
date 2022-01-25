from django.urls import path
from.import views
#from.views import 

urlpatterns = [
    path('aboutpagezetech',views.About_zetech,name="about"),
    #path('club/<str:pk>/participants/remove',views.removeparticipants,name="remove_follower"),

    ]


