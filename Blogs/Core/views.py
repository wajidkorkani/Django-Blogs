from django.shortcuts import render, get_object_or_404
from .models import Blog
# Create your views here.
# This is view for home page. 
def home(request):
    if 'n-o' in request.GET:
        blogs = Blog.objects.all().order_by('-time')
    elif 'o-n'  in request.GET:
        blogs = Blog.objects.all().order_by('time')
    else:
        blogs = Blog.objects.all().order_by('-time')
    template = 'index.html'
    context = {
        'blogs': blogs
        }
    return render(request, template, context)

# This is view for about page 
def about(request, slug, pk):
    blog =  get_object_or_404(Blog, slug=slug, id=pk)
    template = 'about.html'
    context = {
        'blog' : blog
    }
    return render (request, template, context)

# This is view is for searchbar 
def searchbar(request):
    searched = request.GET["searched"]
    blog = Blog.objects.filter(title__icontains=searched)
    title  = Blog.objects.filter(title__iexact=searched)
    categoery  = Blog.objects.filter(categoery__iexact=searched)
    template = 'searchbar.html'
    context = {
        'blog': blog, 
        'blog_title': title, 
        'blog_categoery': categoery
        }
    return render(request, template, context)