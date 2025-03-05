"""Model tests."""

from unittest import TestCase
from models import db, User, Feedback
from app import app

class UserModelTestCase(TestCase):
    """Test User model."""

    def setUp(self):
        """Clean up existing users."""
        db.session.rollback()  # Roll back any failed transactions
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
