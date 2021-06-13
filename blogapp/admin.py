from django.contrib import admin

from .models import Tag, Post, Comment, Author

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'publish')

admin.site.register(Post, PostAdmin)

class CommentAdmin(admin.ModelAdmin):
    list_display = ('post','author', 'email', 'body', 'created', 'parent')
admin.site.register(Comment, CommentAdmin)

admin.site.register(Tag)

admin.site.register(Author)

