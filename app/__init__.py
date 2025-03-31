from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .config import Config

# Initialize extensions
db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)

    # Load config settings from config.py
    app.config.from_object(Config)

    # Connect database and migration tools
    db.init_app(app)
    migrate.init_app(app, db)

    # Import and register blueprint for routes
    from .routes import api_bp
    app.register_blueprint(api_bp)

    return app

# Create and expose the Flask app
app = create_app()
