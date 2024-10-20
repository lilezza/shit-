"""
URL configuration for bache project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf.urls.i18n import i18n_patterns
from django.views.i18n import set_language
from django.contrib import admin
from django.urls import path , include
from home import views as home_views

urlpatterns = i18n_patterns (
    path('admin/', admin.site.urls),
    path('rosetta/', include('rosetta.urls')),
    path('articles/' , include('articles.urls')),
    path('i18n/', set_language , name='set_language'),
    path('' , home_views.HomeView.as_view()) ,
    path('contact/' , home_views.ContactView.as_view() , name = 'contact') ,
    path('about/' , home_views.AboutView.as_view() , name = 'about') ,
    path('accounts/' , include('accounts.urls'))
)
