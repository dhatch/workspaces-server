from flask import request
from flask.ext import restful

class LoginResource(restful.Resource):
    
    def post(self):
        print request.json
        return request.json