from flask.ext.restful import Resource, marshal_with

class ModelResource(Resource):
    """A resource with extended methods for querying objects from a datastore."""
    
    def get_obj(self):
        """Retrive an object from the database."""
        pass
        
    def get_objects(self):
        """Retrieve an iterable of database objects."""
        pass
    
    def get(self, id_=None):
        if id_:
            return self.get_detail(id_)
        else:
            return self.get_list()
    
    def get_detail(self, id_):
        raise NotImplementedError
    
    def get_list(self):
        return get_objects()