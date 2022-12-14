from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email(self):
        """Test creating a new user with an email"""
        email = "email@test.com"
        password = "12345f"
        user = get_user_model().objects.create_user(
            email=email,
            password = password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = "email@TEST.COM"
        user = get_user_model().objects.create_user(
            email=email,
            password = "sdadasd"
        )

        self.assertEqual(user.email, email.lower())
    
    def test_new_user_invalid_email(self):
        """Test creating new user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "sdfsdfsd")
    
    def test_create_new_super_user(self):
        """Test creating a new super user"""
        user = get_user_model().objects.create_superuser(
          'test23@mail.com',
          'sdadasdasd'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
