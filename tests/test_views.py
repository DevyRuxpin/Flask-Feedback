"""View tests."""

import os
from unittest import TestCase
from models import db, User, Feedback

os.environ['DATABASE_URL'] = "postgresql:///flask_feedback_test"

from app import app

db.create_all()

app.config['WTF_CSRF_ENABLED'] = False

class ViewTestCase(TestCase):
    """Test views."""

    def setUp(self):
        """Set up test client and sample data."""
        db.drop_all()
        db.create_all()

        self.client = app.test_client()

        self.testuser = User.register(
            username="testuser",
            password="testuser",
            first_name="Test",
            last_name="User",
            email="test@test.com"
        )
        db.session.commit()

    def tearDown(self):
        """Clean up fouled transactions."""
        db.session.rollback()

    def test_homepage(self):
        """Test homepage redirect."""
        with self.client as client:
            resp = client.get("/")
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "http://localhost/register")
