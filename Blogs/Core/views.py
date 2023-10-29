from django.shortcuts import render
from .models import Blog
# Create your views here.
def home(request):
    if 'n-o' in request.GET:
        blogs = Blog.objects.all().order_by('-time')
    elif 'o-n'  in request.GET:
        blogs = Blog.objects.all().order_by('time')
    else:
        blogs = Blog.objects.all().order_by('-time')
    template = 'index.html'
    context = {'blogs': blogs}
    return render(request, template, context)