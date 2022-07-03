from django import views
from django.shortcuts import render
from .models import *

# Create your views here.
def base(request):
    views_dict = dict()
    views_dict['informations'] = Information.objects.all()
    views_dict['services'] = Services.objects.all()
    views_dict['feedbacks'] = Feedback.objects.all().order_by('-id')
    return views_dict
    
def home(request):
    views_dict = dict()
    return render(request,'index.html' , base(request))
    
def about(request):
    return render(request,'about.html')

def contact(request):
    views_dict = dict()
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
        views_dict = base().update({'message' : "Your Message is send"})
        return render(request,'contact.html',views_dict)
    return render(request,'contact.html',base())

def portfolio(request):
    return render(request,'portfolio.html')

def price(request):
    return render(request,'price.html')

def services(request):
    return render(request,'services.html',base())