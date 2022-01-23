from django.urls import path
from.import views

urlpatterns = [
    path('my/admin-dashboard/', views.admin_dashboard_view,name='admin-dashboard'),
    path('admin-view-users', views.admin_view_user_view,name='admin-view-user'),
    path('admin-view-news', views.admin_view_new_view,name='admin-view-new'),
    path('admin-view-clubs', views.admin_view_clubs_view,name='admin-view-club'),
    path('update-user/<str:pk>/', views.admin_view_upadateuser_view,name='update_user'),
    path('update-news/<str:pk_test>/', views.admin_view_upadatenews_view,name='update_news'),
    path('Add-news', views.admin_view_addnews_view,name='add_news'),
    path('Create New Club', views.admin_view_addclub_view,name='add_club'),
    path('List-Posts', views.admin_view_post_view,name='admin-view-post'),
    path('Student-Leader', views.admin_view_leader_view,name='admin-view-leader'),
    path('Registered-Alumni', views.admin_view_alumniview_view,name='admin-view-alumni'),
    path('Alumni-Forum', views.admin_view_forum_view,name='admin-view-forum'),
    path('Registered-Student', views.admin_view_student_view,name='admin-view-student'),
    path('admin-delete-user/<str:pk>', views.delete_user_view,name='admin-delete-user'),
    path('admin-view-add_user', views.create_user_admin,name='admin-view-add-user'),
    path('admin-delete-news/<str:pk>', views.view_delete_news,name='delete-admin-news'),
    path('update-club-admin/<str:pk>', views.admin_view_editclub_view,name='update_club'),
    path('admin-club-delete/<str:pk>', views.view_club_delete,name='delete_club'),
    path('admin-post-delete/<str:pk>', views.view_delete_post,name='delete_view_post'),
    path('Add_Post_Admin', views.create_post_admin,name='add_Post_admin'),
    path('Create_Student_Leader_Admin', views.create_leader_admin,name='add_Leader_admin'),
    path('admin-leader-delete/<str:pk>', views.view_student_delete,name='delete_view_leader'),
    path('update-student-leader/<str:pk>/', views.update_leader_admin,name='update_leader'),
    path('admin-forum-delete/<str:pk>', views.view_delete_forum,name='delete-forum-view'),
    path('Create_Forum_Admin', views.create_forum_admin,name='add_forum_admin'),
    path('update-forum-admin/<str:pk>', views.update_forum_admin,name='update_forum_admin'),
    path('my/admin-category/',views.admin_catergory_view,name='admin-category'),
    path('Create_leadership', views.add_leader_catergory,name='add_catergory-leader'),
    path('categories_leaders', views.admin_category_leader_view,name='categories_leader'),
    path('Edit_catergory/<str:pk>', views.edit_leader_catergory,name='edit_catergory_leader'),
    path('admin-delete-category/<str:pk>', views.view_catergory_delete,name='delete_view_category'),
    path('categories_post', views.admin_postcats_view,name='categories_post'),
    path('create_post_category', views.add_post_catergory,name='add_catergory-post'),
    path('admin-delete-category/<str:pk>', views.admin_catergorypost_delete,name='delete_category'),
    path('Edit_catergory/<str:pk>', views.postcatergory_edit,name='Post_Catergory_edit'),
    path('Add-About-page', views.admin_about_add,name='admin_aboutadd_view'),
    path('About-page', views. admin_about_view,name='admin_aboutpage_view'),
    path('admin-delete-aboutpage/<str:pk>', views.view_aboutpage_delete,name='delete_about'),
    path('Edit_about_page/<str:pk>', views.admin_about_edit,name='aboutpage_edit'),
    path('Homepage', views.admin_home_view,name='admin_home'),
    path('Zetechteam', views.admin_homezetech_view,name='admin_Zetech'),
    path('create_zetech_team', views.admin_add_Zetech_team,name='add-Zetech_team'),
    path('edit_team_page/<str:pk>', views. admin_edit_Zetech_team,name='edit_Zetechteam'),
    path('admin-delete-team/<str:pk>', views.view_delete_zetechteam,name='delete_team'),
    path('Setting_carsuosel', views.admin_carsouel_view,name='admin_settings_carsusel'),
    path('create_zetech_homeview', views.admin_page_create,name='add-home_view'),
    path('admin-carsuoel-delete/<str:pk>', views.admin_carsuoel_delete,name='delete_carsol'),
    path('edit_carsuoel/<str:pk>',views.admin_edit_Carsuoel,name='edit_Carsuoel'),
    path('Edit_post/<str:pk_test>', views.edit_post_admin,name='Edit_admin_post'),
    


     
    
 
    #path('admin-update-category', views.admin_update_category_view,name='admin-update-category'),
    #path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    #path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    #path('admin-delete-category', views.admin_delete_category_view,name='admin-delete-category'),
    #path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),


    ]