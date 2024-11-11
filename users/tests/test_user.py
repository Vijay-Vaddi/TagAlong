from django.test import TestCase
from django.contrib.auth import get_user_model


class TestUser(TestCase):
    """test cases for users"""

    def test_create_superuser(self):
        """Tests creating a superuser"""
        user = get_user_model().objects.create_superuser(
            'test@example.com',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_create_user(self):
        """test for creating user"""
        user = get_user_model().objects.create_user(
            email="test@example.com",
            password='test123'
        )

        self.assertEqual(user.email,'test@example.com')
        # self.assertEqual(user.password, 'test123')

    def test_create_user_without_email(self):
        """no email provided test"""

        with self.assertRaises(ValueError) as e:
            user = get_user_model().objects.create_user(
                email='',
                password='test123'
            )

