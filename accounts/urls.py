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
    path('logout/', LogoutView.as_view(template_name='logged_out.html', next_page='login'), name='logout'),


]

'''
    #password reset CBV
    path('password-reset/', PasswordResetView.as_view(), name='password_reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', PasswordResetCompleteView.as_view(), name='password_reset_complete'),
'''