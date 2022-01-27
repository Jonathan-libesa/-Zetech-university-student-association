from django.urls import path
from.import views
from django.contrib.auth.decorators import login_required
from.views import PostDetail
urlpatterns = [
    path('Post_views_user/',views.Blog_user,name="blog-home"),
    path('<str:pk>/',login_required(login_url='login')(PostDetail.as_view()),name="post-details"),
    path('Post_Catergory/<str:cats>/',views.categoryview,name="category"),
    #path('load-more-data',views.load_more_data,name='load_more_data'),
    #path('save-comment',views.save_comment,name='save-comment'),
    #path('load-more-data',load_more_data.as_view(),name='load_more_data'),
    ]