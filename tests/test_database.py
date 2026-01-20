from app import create_app
from app.bd import db

def test_database_connection():
    app = create_app()
    # Peewee ferme la connexion après create_tables()
    assert db.is_closed() is True
