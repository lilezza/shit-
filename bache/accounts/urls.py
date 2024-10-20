from django.urls import path , include
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required ,user_passes_test

user_guest = user_passes_test(lambda user:not user.is_authenticated , '/' , None)


urlpatterns = [
    path('login/' , user_guest(auth_views.LoginView.as_view()) , name='login'),
    path('' , include('django.contrib.auth.urls')) ,
    path('profile/' ,(views.profile) , name='profile'),
    path('register/' , views.register , name='register'),
    path('accountlogout', views.user_logout, name='accountlogout')

]

# accounts/login/ [name='login']
# accounts/register/ [name='register']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']
