"""Configurations for pytest."""

import os
from models import db, User, Feedback
from app import app

# Use the GitHub Actions PostgreSQL configuration
if os.environ.get('GITHUB_ACTIONS'):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/flask_feedback_test'
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///flask_feedback_test'

app.config['SQLALCHEMY_ECHO'] = False
app.config['TESTING'] = True
app.config['WTF_CSRF_ENABLED'] = False
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

db.drop_all()
db.create_all()

def create_tables():
    """Create tables."""
    db.create_all()

def drop_tables():
    """Drop tables."""
    db.drop_all()

