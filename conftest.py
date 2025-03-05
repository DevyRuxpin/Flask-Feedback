"""Configurations for pytest."""

import os
import pytest
from models import db, User, Feedback
from app import app

os.environ['DATABASE_URL'] = "postgresql:///flask_feedback_test"
os.environ['SECRET_KEY'] = "test-secret-key"

@pytest.fixture
def client():
    """Client for making test requests."""
    app.config['TESTING'] = True
    app.config['WTF_CSRF_ENABLED'] = False
    
    with app.test_client() as client:
        with app.app_context():
            db.create_all()
            yield client
            db.session.remove()
            db.drop_all()

@pytest.fixture
def test_user():
    """Create test user."""
    user = User.register(
        username="testuser",
        password="testuser",
        first_name="Test",
        last_name="User",
        email="test@test.com"
    )
    db.session.commit()
    return user
