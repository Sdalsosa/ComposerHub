from django.db import models
import uuid
from django.contrib.auth.models import User

STATUS = ((0, "Draft"), (1, "Published"))

# Create your models here.

class Composition(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="compositions_posts", null=True)
    title = models.CharField(max_length=250, unique=True)
    comp_image = models.ImageField(null=True, blank=True, default="hero.png")
    description = models.TextField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    site_link = models.CharField(max_length=2500, null=True, blank=True)
    comp_link = models.CharField(max_length=2500, null=True, blank=True)
    labels = models.ManyToManyField('Label', blank=True)
    likes = models.ManyToManyField(
        User, related_name='composition_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()


class Comment(models.Model):
    composition = models.ForeignKey(Composition, on_delete=models.CASCADE,
                             related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, 
                               related_name="compositions_comments", null=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment : '{self.body}' by {self.author}"


class Label(models.Model):
    name = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)

    def __str__(self):
        return self.name