from django.db import models

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
   
    avatar = models.ImageField(upload_to="user_avatars", blank=True)

   