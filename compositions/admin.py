from django.contrib import admin
from .models import Composition

# Register your models here.


@admin.register(Composition)
class CompositionAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "created_on"]
