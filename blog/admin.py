from django.contrib import admin
from blog.models import * 
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date' 
    
    # fields = ['title','content']
    list_display = ['title' ,'content']

# admin.site.register(Post,PostAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_filter= ["created_date"]
    list_display = ["name","subject","message"]
admin.site.register(Contact,ContactAdmin)