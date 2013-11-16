from flask.ext.restful import Resource, marshal

class ModelResource(Resource):
    """A resource with extended methods for querying objects from a datastore."""
    
    def get_obj(self, id_):
        """Retrive an object from the database."""
        return self.model.query.get(id_)
        
    def get_objects(self):
        """Retrieve an iterable of database objects."""
        return self.model.query.all()
    
    def get(self, id_=None, **kwargs):
        if id_:
            return self.get_detail(id_, **kwargs)
        else:
            return self.get_list(**kwargs)
    
    def get_detail(self, id_, **kwargs):
        obj = self.get_obj(id_)
        return marshal(obj, self.fields)
    
    def get_list(self, **kwargs):
        return [marshal(o, self.fields) for o in self.get_objects()]