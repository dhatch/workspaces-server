from collections import namedtuple

from flask.ext.restful import fields

from . import ModelResource


# temporary shim to hold in for database
User = namedtuple('user', ['first_name', 'last_name', 'username', 'id'])


class UserResource(ModelResource):
    """Represents a user.
    
    Fields:
      - first_name
      - last_name
      - username
      - id
      
    """
    
    fields = {
        'first_name': fields.String,
        'last_name': fields.String,
        'username': fields.String,
        'id': fields.String,
    }
    
    def get_objects(self):
        return map(lambda obj: obj._asdict(), [
            User(first_name="David", 
                 last_name="Hatch", 
                 username="david.hatch",
                 id='1'),
            User(first_name="Michael", 
                 last_name="Menz",
                 username="michael.menz",
                 id='2')
        ])