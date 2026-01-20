from peewee import MySQLDatabase

db = MySQLDatabase(
    'hotel',
    user='root',
    password='motdepasse',
    host='localhost',
    port=3306
)
