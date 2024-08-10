from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return render(request,template_name="index.html")

def about_view(request):
    return render(request,template_name='about.html')

def contact_view(request):
    return render(request,template_name='contact.html')
 