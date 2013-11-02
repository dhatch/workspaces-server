import os

from flask import Flask
from flask.ext import restful, login
from flask.ext.sqlalchemy import SQLAlchemy

from resources import UserResource


app = Flask(__name__)
v1_api = restful.Api(app, prefix='/v1/')

v1_api.add_resource(UserResource, 'user/', defaults={"current_user": True}, 
                    endpoint='currentuser')
v1_api.add_resource(UserResource, 'users/', 'users/<int:id_>/')


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.db = SQLAlchemy(app)

login_manager = login.LoginManager()
login_manager.init_app(app)

from auth import *

if __name__ == '__main__':
    app.run(debug=True)
