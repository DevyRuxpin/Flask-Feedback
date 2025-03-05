"""Seed file to make sample data."""

from models import db, User, Feedback
from app import app

# Create all tables
db.drop_all()
db.create_all()

# Add sample users
u1 = User.register(
    username="testuser",
    password="password",
    first_name="Test",
    last_name="User",
    email="test@test.com"
)

u2 = User.register(
    username="testuser2",
    password="password",
    first_name="Test2",
    last_name="User2",
    email="test2@test.com"
)

db.session.add_all([u1, u2])
db.session.commit()

# Add sample feedback
f1 = Feedback(
    title="Test Feedback",
    content="This is test feedback",
    username="testuser"
)

f2 = Feedback(
    title="Another Feedback",
    content="This is another test feedback",
    username="testuser2"
)

db.session.add_all([f1, f2])
db.session.commit()
