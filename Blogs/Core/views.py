from django.shortcuts import render, get_object_or_404
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

def about(request, slug, pk):
    blog =  get_object_or_404(Blog, slug=slug, id=pk)
    return render (request, 'about.html', {'blog': blog})