from django.urls import path 

from .views import blog, blog_single, post_switch

urlpatterns = [
    path('', blog, name='blog'),
    path('tag/<int:pk_tag>/', blog, name='tag'),
    path('author/<int:pk_auth>/', blog, name='author'),
    path('<slug:post_slug>/', blog_single, name='blog_single'),
    path('<int:pk>', post_switch, name='post_switch'),
 
]
