from django.conf.urls import url

from . import views

# piece to add to regex patterns to match a "slug" [goat-name-like-this]
SLUG = "(?P<pk>[a-z0-9_-]+)"

urlpatterns = [
    url(r"^$", views.GoatListView.as_view(), name='goat_list'),
    url(r"^@add/$", views.GoatCreateView.as_view(), name='goat_add'),
    url(rf"^{SLUG}/$", views.GoatDetailView.as_view(), name='goat_detail'),
    url(rf"^{SLUG}/@edit/$", views.GoatUpdateView.as_view(), name='goat_edit'),
    url(rf"^{SLUG}/@delete/$", views.GoatDeleteView.as_view(), name='goat_delete'),
]

