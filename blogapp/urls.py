from django.urls import path 

from .views import blog, blog_single

urlpatterns = [
    path('', blog),
    path('blog_single', blog_single)
]
