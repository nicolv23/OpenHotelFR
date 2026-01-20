import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY") or "dev-secret-key"

    # Configuration de la base de données
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///hotel.db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
