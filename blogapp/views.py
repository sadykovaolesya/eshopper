from django.shortcuts import render

def blog(request):
    return render(request, "blogapp/blog.html")

def blog_single(request):
    return render(request, "blogapp/blog-single.html")