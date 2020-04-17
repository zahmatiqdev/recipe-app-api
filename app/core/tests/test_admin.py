from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model


class TestAdminSite(TestCase):

    def setUp(self):
        """prepare data for our tests"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email="admin@londonappdev.com",
            password="password1234"
        )
        # force_login ye helper function hast k baes mishe ma betonim login konim
        # bedune inke code ezafi bezanim barash va dakhele django vojod dare
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="test@londonappdev.com",
            password="password1234",
            name="Text user full name"
        )

    def test_users_list(self):
        url = reverse("admin:core_user_changelist")
        res = self.client.get(url)
        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)
