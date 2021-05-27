from django.contrib import admin
from django.urls import path, re_path
from Tracking_app import views_timelog,views_visitors,views_analytics
from django.contrib.auth.decorators import login_required

app_name = "Tracking_app"

urlpatterns = [
    re_path('^$', views_analytics.Main.as_view(), name="report"),
    re_path('User_Details/?$', views_visitors.User_Details.as_view(), name="userdetails"),
    re_path('Time_Details/?$', views_timelog.Time_Details.as_view(), name="timedetails"),
]