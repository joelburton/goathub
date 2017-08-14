from django.utils.text import slugify

from factory import DjangoModelFactory
from factory.declarations import LazyAttribute

from .models import Goat


class GoatFactory(DjangoModelFactory):
    """Sample goat for tests."""

    name = "Happy"
    slug = LazyAttribute(lambda o: slugify(o.name))
    description = LazyAttribute(lambda o: f"Deets about {o.name}")

    class Meta:
        model = Goat
        django_get_or_create = ['slug']
