from flask import Flask

def create_app():
    app = Flask(__name__)

    # Import des routes
    from app.routes.main import main_bp
    app.register_blueprint(main_bp)

    return app
