"""Model tests."""

from unittest import TestCase
from models import db, User, Feedback
from app import app

class UserModelTestCase(TestCase):
    """Test User model."""

    def setUp(self):
        """Clean up existing users."""
        db.session.rollback()
        User.query.delete()
        Feedback.query.delete()
        db.session.commit()

        self.client = app.test_client()

    def tearDown(self):
        """Clean up fouled transactions."""
        db.session.rollback()

    def test_user_model(self):
        """Test basic user model."""
        u = User.register(
            username="testuser",
            password="password",
            first_name="Test",
            last_name="User",
            email="test@test.com"
        )

        db.session.add(u)
        db.session.commit()

        # User should have no feedback
        self.assertEqual(len(u.feedback), 0)
        self.assertEqual(u.username, "testuser")

    def test_valid_registration(self):
        """Test valid user registration."""
        u = User.register(
            username="testuser2",
            password="password",
            first_name="Test",
            last_name="User",
            email="test2@test.com"
        )
        db.session.add(u)
        db.session.commit()

        self.assertEqual(u.username, "testuser2")
        self.assertNotEqual(u.password, "password")
        # Bcrypt strings should start with $2b$
        self.assertTrue(u.password.startswith("$2b$"))

    def test_valid_authentication(self):
        """Test valid user authentication."""
        u = User.register(
            username="testuser3",
            password="password",
            first_name="Test",
            last_name="User",
            email="test3@test.com"
        )
        db.session.add(u)
        db.session.commit()

        valid_auth = User.authenticate("testuser3", "password")
        self.assertIsInstance(valid_auth, User)

    def test_invalid_username(self):
        """Test invalid username authentication."""
        u = User.register(
            username="testuser4",
            password="password",
            first_name="Test",
            last_name="User",
            email="test4@test.com"
        )
        db.session.add(u)
        db.session.commit()

        invalid_auth = User.authenticate("wrongusername", "password")
        self.assertFalse(invalid_auth)

    def test_invalid_password(self):
        """Test invalid password authentication."""
        u = User.register(
            username="testuser5",
            password="password",
            first_name="Test",
            last_name="User",
            email="test5@test.com"
        )
        db.session.add(u)
        db.session.commit()

        invalid_auth = User.authenticate("testuser5", "wrongpassword")
        self.assertFalse(invalid_auth)
