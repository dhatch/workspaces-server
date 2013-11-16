from collections import namedtuple

from flask.ext.restful import fields

from .model import ModelResource


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
        'id': fields.Integer,
    }
    
    def get_list(self, **kwargs):
        if 'current_user' in kwargs:
            # TODO Redo when using database
            return self.get_detail(1)
        else:
            return super(UserResource, self).get_list(**kwargs)
            
    def get_objects(self):
        return [
            User(first_name="David", 
                 last_name="Hatch", 
                 username="david.hatch",
                 id=1),
            User(first_name="Michael", 
                 last_name="Menz",
                 username="michael.menz",
                 id=2)
        ]