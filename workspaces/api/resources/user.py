from collections import namedtuple

from flask.ext.restful import fields

from .model import ModelResource
from ...models import User


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
    
    model = User
    
    def get_list(self, **kwargs):
        if 'current_user' in kwargs:
            # TODO Redo when using database
            return self.get_detail(1)
        else:
            return super(UserResource, self).get_list(**kwargs)