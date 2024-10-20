from django.shortcuts import render
from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView

# Create your views here.
# def index(request):
#     return render(request , 'home.html' ,{
#         'title' : 'Home Page'
#     })

# def about(request):
#     return render(request , 'about.html' ,{
#         'title' : 'About Page'
#     })

# def contact(request):
#     return render(request , 'contact.html' ,{
#         'title' : 'Contact Page'
#     })

class HomeView(TemplateView):
    template_name = 'home.html'

class AboutView(TemplateView):
    template_name = 'about.html'

class ContactView(TemplateView):
    template_name = 'contact.html'
