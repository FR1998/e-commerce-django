from django.contrib.auth.models import AbstractUser, Group, Permission
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
    
     # Add the related_name argument to the groups and user_permissions fields
    groups = models.ManyToManyField(Group, blank=True, related_name='customuser_set')
    user_permissions = models.ManyToManyField(Permission, blank=True, related_name='customuser_set')

    def __str__(self):
        return self.email
