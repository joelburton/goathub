from django.contrib import admin

from .models import Goat


@admin.register(Goat)
class GoatAdmin(admin.ModelAdmin):
    """Goat admin."""
