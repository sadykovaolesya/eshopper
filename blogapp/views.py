from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from .models import Post, Tag

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 


def blog(request, pk=None):

    posts_list = Post.objects.all()
    if pk is not None: 
        posts_list = Post.objects.filter(tags = pk)
       
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    content = {'posts': posts, 'page':page, "media_url": settings.MEDIA_URL}
   
    return render(request, "blogapp/blog.html", content)

def blog_single(request, post_slug):
   
    post = get_object_or_404(Post, slug = post_slug) 
    post_next = Post.objects.filter(pk = post.pk + 1).exists()
    post_pre = Post.objects.filter(pk = post.pk - 1).exists()
   
    content =  {'post':post, 
    "media_url": settings.MEDIA_URL, 
    'post_next':post_next, 
    'post_pre':post_pre, 
  
    }
    return render(request, "blogapp/blog-single.html", content)

def post_switch(request, pk):  
    post = Post.objects.get(pk=pk)
    slug=post.slug
    url = reverse("blog:blog_single", args = (slug,))
    return HttpResponseRedirect(url)


 