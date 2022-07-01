from django import views
from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    views_dict = dict()
    views_dict['feedbacks'] = Feedback.objects.all()
    return render(request,'index.html' , views_dict)
    
def about(request):
    return render(request,'about.html')

def contact(request):
    views_dict = dict()
    views_dict['informations'] = Information.objects.all()
    if request.method == "POST":
        na = request.POST['name']
        em = request.POST['email']
        sub = request.POST['subject']
        mes = request.POST['message']
        data = Contact.objects.create(
            name = na,
            email = em,
            subject = sub,
            message = mes
        )
        data.save()
        views_dict['message'] = 'Your Message Has Sent'
        return render(request,'contact.html',views_dict)


    return render(request,'contact.html',views_dict)

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html')