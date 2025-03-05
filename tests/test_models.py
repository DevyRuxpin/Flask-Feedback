"""Model tests."""

import os
from unittest import TestCase
from sqlalchemy.exc import IntegrityError

from models import db, User, Feedback

os.environ['DATABASE_URL'] = "postgresql:///flask_feedback_test"

from app import app

db.create_all()

class UserModelTestCase(TestCase):
    """Test User model."""

    def setUp(self):
        """Clean up existing users."""
        db.drop_all()
        db.create_all()
        User.query.delete()
        Feedback.query.delete()

    def tearDown(self):
        """Clean up any fouled transaction."""
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

        db.session.commit()

        self.assertEqual(u.username, "testuser")
        self.assertNotEqual(u.password, "password")
        self.assertTrue(User.authenticate("testuser", "password"))
