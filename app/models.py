from peewee import (
    Model,
    CharField,
    BooleanField,
    FloatField,
    ForeignKeyField,
    DateField
)
from .bd import db

class BaseModel(Model):
    class Meta:
        database = db

class Chambre(BaseModel):
    numero = CharField(unique=True)
    type = CharField()
    prix = FloatField()
    disponible = BooleanField(default=True)

class Client(BaseModel):
    nom = CharField()
    email = CharField(unique=True)

class Reservation(BaseModel):
    chambre = ForeignKeyField(Chambre, backref="reservations")
    client = ForeignKeyField(Client, backref="reservations")
    date_debut = DateField()
    date_fin = DateField()
