from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        """Test creating a new user with an email is succesful"""
        email = 'david.keptsman@gmail.com'
        password = 'kahon4258'
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))



    def test_new_user_email_normalized(self):
        """Test the email for new user is normalized"""
        email = 'david.keptsman@GMAIL.com'
        user = get_user_model().objects.create_user(email, 'kahon4258')

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        """Test creating user with no email raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'kahon4258')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'david.keptsman@gmail.com',
            'kahon4258'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
