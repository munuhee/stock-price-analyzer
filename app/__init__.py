from flask import Flask
from .api.stock_routes import api_bp  # Import the blueprint

def create_app():
    app = Flask(__name__)

    # Register the API blueprint
    app.register_blueprint(api_bp, url_prefix='/api')

    return app
