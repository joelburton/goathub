from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
from django.views import generic
from braces import views as braces

from .models import Goat


class GoatListView(braces.SetHeadlineMixin,
                   generic.ListView):
    """List goats."""

    model = Goat
    headline = "Goat List"
    paginate_by = 5


class GoatDetailView(braces.SetHeadlineMixin,
                     generic.DetailView):
    """Detail about a goat."""

    model = Goat

    def get_headline(self):
        """Page headline is goat name."""

        return str(self.object)


class GoatCreateView(PermissionRequiredMixin,
                     braces.SetHeadlineMixin,
                     braces.FormValidMessageMixin,
                     generic.CreateView):
    """Add a goat."""

    model = Goat
    fields = '__all__'
    permission_required = 'goats.add_goat'
    headline = "Add Goat"
    form_valid_message = "Goat added."


class GoatUpdateView(PermissionRequiredMixin,
                     braces.SetHeadlineMixin,
                     braces.FormValidMessageMixin,
                     generic.UpdateView):
    """Edit a goat."""

    model = Goat
    fields = '__all__'
    permission_required = 'goats.change_goat'
    form_valid_message = "Updated."

    def get_headline(self):
        """Page headline is goat name."""

        return f"Update {self.object}"


class GoatDeleteView(PermissionRequiredMixin,
                     braces.SetHeadlineMixin,
                     braces.FormValidMessageMixin,
                     generic.DeleteView):
    """Delete a goat."""

    model = Goat
    permission_required = 'goats.delete_goat'
    form_valid_message = 'Deleted.'
    success_url = reverse_lazy('goat_list')

    def get_headline(self):
        """Page headline is goat name."""

        return f"Delete {self.object}"
