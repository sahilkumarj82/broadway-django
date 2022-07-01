from django.urls import path
from .views import*

urlpatterns = [
    path('', home,name = 'home.html'),
    path('about/',about,name = 'about.html'),
    path('contact/',contact,name = 'contact'),
    path('portfolio/',portfolio,name = 'portfolio'),
    path('price/',price,name = 'price'),
    path('services/',services,name = 'services'),
]
