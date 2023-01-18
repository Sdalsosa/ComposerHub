from django.contrib import admin
from .models import Composition, Comment

# Register your models here.

admin.site.register(Comment)

@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'created_on']