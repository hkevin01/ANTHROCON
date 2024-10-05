from flask import Flask
from .config import Config
from .utils.database import db

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from .routes.auth_routes import auth_bp
    from .routes.event_routes import event_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(event_bp)

    return app