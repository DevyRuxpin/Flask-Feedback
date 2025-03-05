"""Flask app configuration."""

import os

class Config:
    """Base configuration."""
    
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev')
    SQLALCHEMY_DATABASE_URI = os.environ.get(
        'DATABASE_URL', 'postgresql:///flask-feedback')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False

class TestConfig(Config):
    """Test configuration."""
    
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql:///flask_feedback_test'
    WTF_CSRF_ENABLED = False
    DEBUG_TB_HOSTS = ['dont-show-debug-toolbar']
