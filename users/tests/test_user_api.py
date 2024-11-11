"""Tests for user API"""

from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status

# api url we're testing
CREATE_USER_URL = reverse('user:create_user')

# helper function to create a user that we'll use for testing
def create_user(**params):
    """Create and return a new user"""
    return get_user_model().objects.create_user(**params)


# breakdown tests between endpoints that require auth and don't
class PublicUserApiTests(TestCase):
    """Test the public features of the user API"""
    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test creating a user is successfull"""
        payload = {
            'email':'test@example.com',
            'password':'test123',
            'name':"Test Name",
        }
        response = self.client.post(CREATE_USER_URL,payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        # to ensure we dont accidentally send the password in response
        self.assertNotIn('password',response.data)

    def test_user_with_email_exists_error(self):
        """Test error if user with email already exists"""
        payload = {
            'email':'test@example.com',
            'password':'test123',
            'name':"Test Name",
        }
        create_user(**payload)
        response = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Test an error is returned if password is less than 5 chars"""
        