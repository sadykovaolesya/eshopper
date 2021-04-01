from django.urls import path

from .views import   logout, all_auth, login, register

urlpatterns = [
    path('all_auth/', all_auth, name='all_auth'),
    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', register, name='register'),
]
