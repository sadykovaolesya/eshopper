
from django.urls import reverse

from django.db import models
from django.db.models import Exists

from authnapp.models import CustomUser

class Tag(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Post(models.Model):
    
    title = models.CharField( max_length=64, unique=True )
    content = models.TextField()
    publish = models.DateTimeField(auto_now_add=True, db_index=True)
    author = models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)
    image = models.ImageField()
    likes = models.IntegerField(default=0)
    voice = models.IntegerField(default=0)
    slug = models.SlugField(max_length=250)

    class Meta:
        ordering = ['-publish']
    
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        
        return reverse("blog:blog_single", args=[self.slug])

    def count_full_stars(self):
        star_full = round(self.likes/self.voice)
        return range(star_full)

    def count_emp_stars(self):
        star_full = round(self.likes/self.voice)
        star_empty = 5 - star_full
        return range(star_empty)

   
      
class Comment(models.Model):
    
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    author =models.CharField(max_length=64)
    email = models.EmailField()
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.author}, ({self.post})"
