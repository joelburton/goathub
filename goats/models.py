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

    photo = models.ImageField(
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

    def get_absolute_url(self):
        """Canonical URL for goat."""

        return reverse("goat_detail", kwargs={'pk': self.slug})
