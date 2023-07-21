from django.contrib.auth.models import AbstractUser
from django.db import models
from user.manager import CustomUserManager


class CustomUser(AbstractUser):
    username = None
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15,unique=True)
    address = models.TextField()
    profile_picture = models.ImageField(upload_to="profile_picture", blank=True)
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
