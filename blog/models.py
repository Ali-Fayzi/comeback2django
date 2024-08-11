from django.db import models

# Create your models here.
class Post(models.Model):
    # image
    # author
    title = models.CharField(verbose_name="Title",name="title",primary_key=False,max_length=60)
    content = models.TextField(verbose_name="Content",name="content",primary_key=False)
    # tag
    # category
    counted_views = models.IntegerField(default=0)
    status = models.BooleanField(default=False)
    published_date = models.DateTimeField(null=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now = True)
    
    
    class Meta:
        ordering = ['created_date']
        verbose_name = "پست"
        verbose_name_plural = "پست ها "
    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    
    name = models.CharField(max_length=255)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['created_date']
        verbose_name = 'تماس با ما '
        verbose_name_plural = "تماس با ما ها "
    def __str__(self):
        return self.subject