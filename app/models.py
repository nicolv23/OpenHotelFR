from peewee import Model, CharField, BooleanField, FloatField, ForeignKeyField, DateField
from .bd import db

class BaseModel(Model):
    class Meta:
        database = db
