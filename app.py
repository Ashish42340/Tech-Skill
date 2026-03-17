"""
Main Flask Application
Tech Skills Checker - Main entry point
"""

from flask import Flask
from flask_login import LoginManager
from models import db, User
from routes import auth_bp, main_bp, api_bp
from config import Config
import os

def create_app():
    """
    Flask application factory
    """
    app = Flask(__name__)
    app.config.from_object(Config)
    
    # Initialize database
    db.init_app(app)
    
    # Initialize Flask-Login
    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Pehle login karo!'
    login_manager.login_message_category = 'warning'
    
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Register blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(api_bp)
    
    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()
    
    return app


if __name__ == '__main__':
    app = create_app()
    
    print("="*60)
    print("🚀 Tech Skills Checker Starting...")
    print("="*60)
    print("📱 Open: http://127.0.0.1:5000")
    print("👤 Login: admin / admin123")
    print("="*60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)