from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User

def m(request):
    print(request.user)
    return render(request,'Tracking_app/index.html')
