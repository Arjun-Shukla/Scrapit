from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def rates(request):
    return render(request, 'rates.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def usersignup(request):
    return render(request, 'usersignup.html')