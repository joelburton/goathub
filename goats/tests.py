from django.contrib.auth.models import User, Permission
from django.test import TestCase

from goats.factories import GoatFactory


class GoatModelTest(TestCase):
    """Test that we can create/edit goats."""

    def setUp(self):
        self.goat = GoatFactory()
        self.goat2 = GoatFactory(name="Bob")

    def test_model(self):
        self.assertEqual(self.goat.slug, "happy")
        self.assertEqual(self.goat.description, "Deets about Happy")

    def test_model2(self):
        self.assertEqual(self.goat2.slug, "bob")
        self.assertEqual(self.goat2.description, "Deets about Bob")


class GoatViewTest(TestCase):
    """Test views for goats."""

    def setUp(self):
        self.goat = GoatFactory()

    def test_list(self):
        response = self.client.get("/")
        self.assertContains(response, "<p>Deets about Happy</p>", html=True)

    def test_detail(self):
        response = self.client.get("/happy/")
        self.assertContains(response, "<p>Deets about Happy</p>", html=True)


class GoatEditViewTest(TestCase):
    """Test editing views for goats."""

    def setUp(self):
        self.goat = GoatFactory()

        # create staff user for testing security
        perm = Permission.objects.get(codename='change_goat')
        self.staff = User.objects.create_user("staff", password="staff")
        self.staff.user_permissions.add(perm)

    def test_anon_cannot_edit(self):
        # doesn't see edit button
        response = self.client.get("/happy/")
        self.assertNotContains(response, "Edit")

        # can't get to edit form
        response = self.client.get("/happy/@edit/")
        self.assertNotContains(response, "Update Happy", status_code=302)

        # can't use edit form
        response = self.client.post("/happy/@edit/", follow=True,
                                    data={'name': self.goat.name,
                                          'slug': self.goat.slug,
                                          'description': 'NEW'})
        self.assertNotContains(response, "Updated", status_code=404)

    def test_staff_can_edit(self):
        self.client.force_login(self.staff)

        # can see button
        response = self.client.get("/happy/")
        self.assertContains(response, "Edit")

        # can get to edit form
        response = self.client.get("/happy/@edit/")
        self.assertContains(response, "Update Happy")

        # can use edit form
        response = self.client.post("/happy/@edit/", follow=True,
                                    data={'name': self.goat.name,
                                          'slug': self.goat.slug,
                                          'description': 'NEW'})
        self.assertContains(response, "Updated", status_code=200)
        self.assertContains(response, "NEW")
