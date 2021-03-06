from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
app_name='nemo'

urlpatterns = [
    path('', views.homepage,name='home'),
    path('register', views.register_user,name = "register"),
    path('login', views.login_user,name='login_user'),
    path('logout', views.logout_user),
    path('admins/users',views.get_users),
    path('admins/admins', views.get_admins),
    path('promote_user/<int:user_id>', views.promote_user),
    path('demote_user/<int:user_id>', views.demote_user),
    path('profile', views.profile),
    path('password_change', auth_views.PasswordChangeView.as_view(
        template_name='userlogin/password_change.html')),
    path('password_change_done', auth_views.PasswordChangeView.as_view(
        template_name='userlogin/password_change_done.html'), name='password_change_done'),

]