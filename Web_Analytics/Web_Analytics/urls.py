"""Web_Analytics URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, re_path
from django.conf.urls import url, include
# from Tracking_app import views
from django.conf import settings
from Tracking_app import views_visitors,views_timelog,views_analytics


urlpatterns = [
    # path('', views.m, name='main'),
    re_path('^$', views_analytics.Main.as_view(), name="login"),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    url(r'Web_Analytics/', include('Tracking_app.urls', namespace='Tracking_app')),
]
