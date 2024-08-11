from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home_view(request):
    data = {
        'title':'Home Page',
    }
    return render(request,template_name="index.html",context=data)

def about_view(request):
    data = {
        'title':'About Page',
    }
    return render(request,template_name='about-me.html',context=data)

def contact_view(request):
    data = {
        'title':'Contact'
    }
    return render(request,template_name='contact.html',context=data)
 