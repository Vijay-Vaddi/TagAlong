"""Test case for django admin modifications"""
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse

class TestAdminSite(TestCase):
    """Test for django admin"""

    def setUp(self):
        """create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email='admin@example.com',
            password='testpass123'
        )

        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            email="user@example.com",
            password='testpass123',
            first_name = 'test_user',
        )
        # self.client.force_login(self.user)

    def test_user_list(self):
        """test that users are listed on the page"""
        url = reverse("admin:users_user_changelist")
        response = self.client.get(url)

        self.assertContains(response, self.user.first_name)
        self.assertContains(response, self.user.email)

    def test_edit_user_page(self):
        """test edit user page in admin"""
        url = reverse('admin:users_user_change', args=[self.user.id])
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

    def test_create_user_page(self):
        """test add user page in admin"""
        url = reverse('admin:users_user_add')
        response = self.client.get(url)

        self.assertEqual(response.status_code,200)