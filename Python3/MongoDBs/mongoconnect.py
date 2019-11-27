import mongoengine
from datetime import datetime

def global_connect():
    mongoengine.register_connection(alias='core',name='tests')

class Snake:
    registered_date = mongoengine.DateTimeField(default=datetime.now())
    species = mongoengine.StringField(required=True)
    

