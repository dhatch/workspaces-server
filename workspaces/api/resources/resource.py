from flask import request
from flask.ext import restful


class Resource(restful.Resource):
    
    def post_data(self):
        if request.json:
            return request.json
        else:
            return request.form