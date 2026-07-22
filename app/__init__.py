from flask import Flask
from dotenv import load_dotenv
import os

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("JWT_SECRET_KEY")

    
    from app.auth.routes import auth_bp
    # from app.agenda.routes import agenda_bp
    # from app.mock_api.routes import mock_api_bp

    app.register_blueprint(auth_bp)
    # app.register_blueprint(agenda_bp)
    # app.register_blueprint(mock_api_bp, url_prefix="/mock-api")

    return app