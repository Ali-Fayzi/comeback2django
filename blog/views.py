from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    return HttpResponse(content='Home Page')

def about_view(request):
    return HttpResponse(content="About")

def contact_view(request):
    return HttpResponse(content="Contact")