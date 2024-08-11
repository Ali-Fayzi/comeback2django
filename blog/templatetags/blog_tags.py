from django import template
from blog.models import *
register = template.Library()


@register.inclusion_tag(filename='lastest-post.html',name='lastest_post')
def lastest_post():
    post = Post.objects.all() 
    return {"post":post}