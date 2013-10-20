from flask.ext.restful import fields
from . import ModelResource

class UserResource(ModelResource):
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
    
    def get_objects(self):
        return [
            {
                "first_name": "David",
                "last_name": "Hatch", 
                "username": "david.hatch"
            },
            {
                "first_name": "Michael", 
                "last_name": "Menz",
                "username": "michael.menz"
            }
        ]