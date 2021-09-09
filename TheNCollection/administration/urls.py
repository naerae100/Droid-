from django.urls import path
from django.urls import path
from . import views


urlpatterns = [
    path('',views.homepage),
    path('admins/users',views.get_users),
    path('admins/admins', views.get_admins),
    path('promote_user/<int:user_id>', views.promote_user),
    path('demote_user/<int:user_id>', views.demote_user),
    path('admins/getprofile', views.get_profile),
    path('admins/getpost', views.get_post),
    path('admins/postdelete/<int:post_id>', views.delete_post),
]