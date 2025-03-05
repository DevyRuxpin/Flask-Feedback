"""View tests."""

from unittest import TestCase
from models import db, User, Feedback
from app import app

class ViewTestCase(TestCase):
    """Test views."""

    def setUp(self):
        """Create test client and add sample data."""
        db.session.rollback()
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
            resp = c.get("/", follow_redirects=False)
            self.assertEqual(resp.status_code, 302)
            self.assertEqual(
                resp.headers["Location"].rpartition("/")[2], 
                "register"
            )

    def test_register_form(self):
        """Test register form display."""
        with self.client as c:
            resp = c.get("/register")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("Register", html)

    def test_login_form(self):
        """Test login form display."""
        with self.client as c:
            resp = c.get("/login")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn("Login", html)

    def test_user_show(self):
        """Test user profile display."""
        with self.client as c:
            with c.session_transaction() as sess:
                sess["username"] = self.testuser.username
            
            resp = c.get(f"/users/{self.testuser.username}")
            self.assertEqual(resp.status_code, 200)
            html = resp.get_data(as_text=True)
            self.assertIn(self.testuser.username, html)

    def test_unauthorized_access_user_profile(self):
        """Test unauthorized access to user profile."""
        with self.client as c:
            resp = c.get(f"/users/{self.testuser.username}", follow_redirects=True)
            self.assertEqual(resp.status_code, 401)

    def test_unauthorized_access_feedback(self):
        """Test unauthorized access to feedback page."""
        with self.client as c:
            resp = c.get(f"/users/{self.testuser.username}/feedback/new", 
                        follow_redirects=True)
            self.assertEqual(resp.status_code, 401)

