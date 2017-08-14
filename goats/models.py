from django.db import models
from django.urls import reverse


class Goat(models.Model):
    """Goat."""

    name = models.CharField(
        max_length=50,
        unique=True,
    )

    slug = models.SlugField(
        max_length=20,
        primary_key=True,
    )

    description = models.TextField(
        blank=True,
    )

    class Meta:
        ordering = ['name']

    def __str__(self):
        """Default name of goat is the name field."""

        return self.name

    def get_absolute_url(self):
        """Canonical URL for goat is the detail page for it."""

        return reverse("goat_detail", kwargs={'pk': self.slug})
