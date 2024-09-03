from django.urls import path,include
from . import views
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)

app_name = 'job'
urlpatterns = [
    path('signup',views.signup, name='signup'), 
    path('profile/',views.profile, name='profile'),
    path('profile/edit',views.profile_edit, name='profile_edit'),
    #path('logout', views.logout_view, name='logout'),
   


]

