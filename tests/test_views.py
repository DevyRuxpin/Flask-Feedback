"""View tests."""

from unittest import TestCase
from models import db, User, Feedback
from app import app

class ViewTestCase(TestCase):
    """Test views."""

    def setUp(self):
        """Create test client and add sample data."""
        db.session.rollback()  # Roll back any failed transactions
        User.query.delete()
        Feedback.query.delete()
        db.session.commit()

        self.client = app.test_client()

        self.testuser = User.register(
            username="testuser",
            password="testuser",
            first_name="Test",
            last_name="User",
            email="test@test.com"
        )
        db.session.add(self.testuser)
        db.session.commit()

    def tearDown(self):
        """Clean up fouled transactions."""
        db.session.rollback()

    def test_homepage_redirect(self):
        """Test homepage redirect."""
        with self.client as c:
            resp = c.get("/")
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(resp.location, "/register")
