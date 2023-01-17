from django.contrib import admin
from .models import Composition, Comment, Label

# Register your models here.

admin.site.register(Composition)
admin.site.register(Comment)
admin.site.register(Label)