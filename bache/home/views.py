from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
def index(request):
    return render(request , 'home.html' ,{
        'title' : 'Home Page'
    })

def about(request):
    return render(request , 'about.html' ,{
        'title' : 'About Page'
    })

def contact(request):
    return render(request , 'contact.html' ,{
        'title' : 'Contact Page'
    })
