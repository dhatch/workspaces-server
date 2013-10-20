from flask.ext.restful import fields
from . import ModelResource


class User(ModelResource):
    """Represents a user.
    
    Fields:
      - first_name
      - last_name
      - username
      
    """
    
    fields = {
        'first_name': fields.String,
        'last_name': fields.String,
        'username': fields.String
    }
    
    