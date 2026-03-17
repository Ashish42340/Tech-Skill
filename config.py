"""
Configuration file for Tech Skills Checker
Ye file settings store karti hai
"""

import os
from datetime import timedelta

# Base directory (jahan ye file hai)
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    """
    Application configuration settings
    """
    
    # Secret key for session management
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key-change-in-production'
    
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'database', 'techskills.db')
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Session configuration
    PERMANENT_SESSION_LIFETIME = timedelta(days=7)
    SESSION_COOKIE_SECURE = False  # Set True in production with HTTPS
    SESSION_COOKIE_HTTPONLY = True
    SESSION_COOKIE_SAMESITE = 'Lax'
    
    # Remember me configuration
    REMEMBER_COOKIE_DURATION = timedelta(days=30)
    REMEMBER_COOKIE_SECURE = False  # Set True in production
    REMEMBER_COOKIE_HTTPONLY = True
    
    # Upload configuration (agar future mein file upload chahiye)
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    UPLOAD_FOLDER = os.path.join(basedir, 'uploads')
    
    # Scraper configuration
    SCRAPER_TIMEOUT = 10  # seconds
    SCRAPER_DELAY = 2  # seconds between requests
    
    # Debug mode
    DEBUG = True