from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Signup

# Create your views here.

def index(request):
    return render(request, 'index.html')

def rates(request):
    return render(request, 'rates.html')

def userlogin(request):
    return render(request, 'userlogin.html')

def usersignup(request):
    if request.method == "POST":
        f_name = request.POST.get('f_name')
        gender = request.POST.get('gender')
        contactno = request.POST.get('contactno')   
        email = request.POST.get('email')
        address = request.POST.get('address')
        state = request.POST.get('state')
        district = request.POST.get('district')
        city = request.POST.get('city')
        password = request.POST.get('password')

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
            password=password
            )

            subject = "Successfully Account Created"
            message = render_to_string('email/wel_email.html',{
                'username' : f_name,
                
            })
            email = EmailMessage(
                subject,
                message,
                "scrapitkart@gmail.com",
                [str(email)]
            )
            email.content_subtype = "html"
            email.send()
            return redirect('userlogin')
    


    return render(request, 'usersignup.html')