from django.db import models
import uuid
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from users.models import Profile


# From Taggit docs to work with UUID.


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    # If you only inherit GenericUUIDTaggedItemBase, you need to define
    # a tag field. e.g.
    # tag = models.ForeignKey(Tag, related_name="uuid_tagged_items",
    # on_delete=models.CASCADE)

    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")

    # Composition model


class Composition(models.Model):
    owner = models.ForeignKey(Profile,
                              null=True, blank=True,
                              on_delete=models.SET_NULL)
    id = models.UUIDField(
                          default=uuid.uuid4,
                          unique=True,
                          primary_key=True,
                          editable=False
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE,
        related_name="compositions_posts",
        null=True
    )
    title = models.CharField(max_length=250, unique=True)
    comp_image = models.ImageField(null=True, blank=True,
                                   default="images/hero.png")
    description = models.TextField(null=True, blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    created_on = models.DateTimeField(auto_now_add=True)
    site_link = models.CharField(max_length=250, null=True, blank=True)
    comp_link = models.CharField(max_length=250, null=True, blank=True)
    tags = TaggableManager(through=UUIDTaggedItem, blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()
