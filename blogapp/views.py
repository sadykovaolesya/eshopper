from django.http import request
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
from django.conf import settings
from django.urls import reverse
from .models import Post, Tag, Comment

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger 
from .forms import CommentForm, HiddenForm

def blog(request, pk_tag=None, pk_auth=None):

    posts_list = Post.objects.all()
    if pk_tag is not None: 
        posts_list = Post.objects.filter(tags = pk_tag)
    if pk_auth is not None: 
        posts_list = Post.objects.filter(author = pk_auth)
       
    paginator = Paginator(posts_list, 2)
    page = request.GET.get('page')
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    content = {'posts': posts, 'page':page, "media_url": settings.MEDIA_URL}
   
    return render(request, "blogapp/blog.html", content)


def save_id(request):
    parent_obj_id = int(request.GET['id'])
    print(parent_obj_id)


def blog_single(request, post_slug):
    
    post = get_object_or_404(Post, slug = post_slug) 
    post_next = Post.objects.filter(pk = post.pk + 1).exists()
    post_pre = Post.objects.filter(pk = post.pk - 1).exists()
    comments = Comment.objects.filter(active=True,parent__isnull=True, post = post.pk)
    count_comments = Comment.objects.filter(active=True,parent__isnull=True, post = post.pk).count()
     
    if  request.method == 'POST':
        comment_form = CommentForm(data=request.POST)  
        
        if comment_form.is_valid(): 
            parent_obj = None 
            try:  
               parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    replay_comment = comment_form.save(commit=False)
                    replay_comment.parent = parent_obj       
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
            return HttpResponseRedirect(post.get_absolute_url())
    else:
        comment_form = CommentForm()
       
    content =  {'post':post, 
    "media_url": settings.MEDIA_URL, 
    'post_next':post_next, 
    'post_pre':post_pre, 
    'comments':comments,
    'comment_form':comment_form,
    'count_comments':count_comments,
    
    }
    return render(request, "blogapp/blog-single.html", content)

def post_switch(request, pk):  
    post = Post.objects.get(pk=pk)
    slug=post.slug
    url = reverse("blog:blog_single", args = (slug,))
    return HttpResponseRedirect(url)


 