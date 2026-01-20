from flask import Flask
from .bd import db
from .models import Chambre, Client, Reservation
from .routes.main import main_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object("config.Config")

    # Connexion à la base
    db.connect()
    db.create_tables([Chambre, Client, Reservation])
    db.close()

    app.register_blueprint(main_bp)

    return app
