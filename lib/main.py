from peewee import *
from datetime import date
db = PostgresqlDatabase('contacts', user='postgres', password='',
                        host='localhost', port=5432)

db.connect()


class BaseModel(Model):
    class Meta:
        database = db
        
class Contacts(BaseModel):
    name = CharField()
    birthday = DateField()
    
db.create_tables([Contacts])