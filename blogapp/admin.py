from django.contrib import admin

from .models import Tag, Post, Comment

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'email', 'body', 'created')
admin.site.register(Comment, CommentAdmin)

admin.site.register(Tag)

