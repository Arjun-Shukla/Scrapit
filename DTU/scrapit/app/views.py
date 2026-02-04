from urllib import request
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Signup
from django.contrib.auth import authenticate, login
from django.contrib import messages
from .models import Pickup
from .models import contactus


# Create your views here.


def index(request):
    return render(request, "index.html")


def rates(request):
    return render(request, "rates.html")


def userlogin(request):
    if request.method != "POST":
        return render(request, "userlogin.html")

    email = request.POST.get("email")
    password = request.POST.get("password")
    user = Signup.objects.filter(email=email, password=password).first()

    if user is not None:
        # Since not using Django auth, just redirect
        messages.success(request, "Login successful! Redirecting to home page.")
        return render(request, "userlogin.html")
    else:
        messages.error(request, "User not found. Please sign up.")
        return render(request, "userlogin.html")


def usersignup(request):
    if request.method == "POST":
        f_name = request.POST.get("f_name")
        gender = request.POST.get("gender")
        contactno = request.POST.get("contactno")
        email = request.POST.get("email")
        address = request.POST.get("address")
        state = request.POST.get("state")
        district = request.POST.get("district")
        city = request.POST.get("city")
        password = request.POST.get("password")

        if f_name and email and password:
            Signup.objects.create(
                f_name=f_name,
                gender=gender,
                contactno=contactno,
                email=email,
                address=address,
                state=state,
                district=district,
                city=city,
                password=password,
            )

            subject = "Successfully Account Created"
            message = render_to_string(
                "email/wel_email.html",
                {
                    "username": f_name,
                },
            )
            email = EmailMessage(
                subject, message, "scrapitkart@gmail.com", [str(email)]
            )
            email.content_subtype = "html"
            email.send()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect("userlogin")

    return render(request, "usersignup.html")


def training(request):
    return render(request, "training.html")


def pickup(request):
    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        date = request.POST.get("date")
        time_slot = request.POST.get("time_slot")
        items = request.POST.get("items")

        Pickup.objects.create(
            name=name,
            address=address,
            date=date,
            time_slot=time_slot,
            items=items,
        )

        messages.success(request, "Pickup request submitted successfully!")
        return redirect("pickup")
    return render(request, "pickup.html")


def firstv(request):
    return render(request, "firstv.html")


def secondv(request):
    return render(request, "secondv.html")


def thirdv(request):
    return render(request, "thirdv.html")


def aboutus(request):
    return render(request, "aboutus.html")


def Contactus(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")

        contactus.objects.create(
            name=name,
            mobile=mobile,
            email=email,
        )

        messages.success(
            request, "Thank you for contacting us! We will get to touch you soon."
        )
        return redirect("index")
    return render(request, "index.html")


def secondhand(request):
    return render(request, "secondhand.html")