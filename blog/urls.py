from django.urls import path
from blog.views import * 

app_name = "blog"
urlpatterns = [
    path('',home_view , name='home_page'),
    path('about/',about_view,name='about_page'),
    path('contact/',contact_view,name='contact_page'),
    path('posts/',show_posts,name="posts"),
    path('post/<str:title>',show_post , name="post"),
]