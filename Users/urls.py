from django.urls import path
from django.contrib.auth import views as auth_views
from.import views
from.views import CompletePasswordReset,RequestPasswordReset
urlpatterns = [
   path(' student_registration/',views.studentpage,name="student_page"),
   path(' alumnae_registration/',views.alumnipage,name="alumni_page"),
   path('login/',views.loginpage,name="login"),
   path('logout/',views.logoutUser,name="logout"),
   path('activate-user/<uidb64>/<token>',views.activate_user, name='activate'),
   path('profile/<str:pk>', views.userProfile, name="user-profile"),
   path('update-user-view', views.updateUser, name="update-user"),
   path('account_setting_user',views.account_Setting,name="account"),
   path('Add_post',views.ADD_USER_POST,name="add_post"),
   path('Delete_Post/<str:pk>',views.delete_post_user,name="delete_user_post"),
   path('profile_view_user', views.profile_view_user, name="user_profile"),
   path('request-password-reset-link',RequestPasswordReset.as_view(),name="request-password"),
   path('set-new-password/<uidb64>/<token>',CompletePasswordReset.as_view(), name='reset-user-password'),
   ]