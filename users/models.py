from django.db import models
from django.contrib.auth.models import User
import uuid
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver


# Profile model

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(max_length=250, blank=True, null=True)
    username = models.CharField(max_length=250, blank=True, null=True)
    about = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(blank=True, null=True, upload_to="profilePics/", default="profilePics/profile.png")
    website = models.CharField(max_length=250, blank=True, null=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.user.username)