"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    #accounts before the admin
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls',namespace='accounts')),
    path('admin/', admin.site.urls),
    path('jobs/', include('job.urls',namespace = 'jobs')),
    path('', lambda request: redirect('jobs:available_jobs')),
    path('contact-us/', include('contact.urls',namespace = 'contact')),
    path('blog/', include('blog.urls')),
    #api
    path('api/reviews/', include('reviews.urls')), 
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)