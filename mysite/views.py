from django.http import HttpResponse,JsonResponse 
def about_us(request):
    return HttpResponse(content="About Us")

def about_us_js(request):
    return JsonResponse(data={"name":"ali"})
