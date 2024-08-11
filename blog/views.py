from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

# Create your views here.
from blog.models import Post
def home_view(request):
    posts = Post.objects.filter(status=1)
    data = {
        'title':'Home Page',
        'posts':posts
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
 
def show_posts(request):
    posts = Post.objects.filter(status=1)
    return render(request,template_name="blog.html",context={"posts":posts})
def show_post(request,title):
    # data = Post.objects.filter(title=title).get()
    data = get_object_or_404(Post,title=title,status=1)
    return render(request=request,template_name="single.html",context={'data':data})