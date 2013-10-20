from flask import Flask
from flask.ext import restful

from resources import UserResource


app = Flask(__name__)
v1_api = restful.Api(app, prefix='/v1/')

v1_api.add_resource(UserResource, 'users/')

if __name__ == '__main__':
    app.run(debug=True)