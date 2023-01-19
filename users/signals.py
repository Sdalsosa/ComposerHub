from django.contrib.auth.models import User
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from .models import Profile


# Using signals to create a profile when user created

@receiver(post_save, sender=User)
def createUserProfile(sender, instance, created, **kwargs):
    if created:
        user = instance
        profile = Profile.objects.create(
            user=user,
            username=user.username,
        )

# Using signals to delete a user when profile deleted

@receiver(post_delete, sender=Profile)
def deleteUser(sender, instance, **kwargs):
    user = instance.user
    user.delete()