from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("rates/", views.rates, name="rates"),
    path("userlogin/", views.userlogin, name="userlogin"),
    path("usersignup/", views.usersignup, name="usersignup"),
    path("training/", views.training, name="training"),
    path("pickup/", views.pickup, name="pickup"),
    path("firstv/", views.firstv, name="firstv"),
    path("secondv/", views.secondv, name="secondv"),
    path("thirdv/", views.thirdv, name="thirdv"),
    path("aboutus/", views.aboutus, name="aboutus"),
    path("contactus/", views.Contactus, name="contactus"),
    path("secondhand/", views.secondhand, name="secondhand"),
]
