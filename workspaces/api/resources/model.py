from flask.ext.restful import Resource, marshal

class ModelResource(Resource):
    """A resource with extended methods for querying objects from a datastore."""
    
    def get_obj(self):
        """Retrive an object from the database."""
        pass
        
    def get_objects(self):
        """Retrieve an iterable of database objects."""
        pass
    
    def get(self, id_=None, **kwargs):
        if id_:
            return self.get_detail(id_, **kwargs)
        else:
            return self.get_list(**kwargs)
    
    def get_detail(self, id_, **kwargs):
        obj = filter(lambda obj: obj.id == id_, 
                     self.get_objects())[0]
        return marshal(obj._asdict(),
                       self.fields)
    
    def get_list(self, **kwargs):
        return map(lambda obj: obj._asdict(), self.get_objects())