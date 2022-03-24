from django.urls import path
from.import views
#from.views import add_post
urlpatterns = [
    #path('add post/',add_post.as_view(),name="add_post"),
    path('voting',views. poll_home,name="polls"),
    path('candidate/<int:pos>/', views.candidateView, name='candidate'),
    path('my/Results/', views.resultView, name='result_page'),
    #path('my/votes_law', views.index, name='result'),
    #path('my/polls', views.vote, name='polls_vote'),
    #path('position/', views.positionView, name='position'),
    ] 