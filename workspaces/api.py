import os

from flask import Flask
from flask.ext import restful, login
from flask.ext.sqlalchemy import SQLAlchemy

from resources import UserResource, LoginResource


app = Flask(__name__)
v1_api = restful.Api(app, prefix='/v1/')

v1_api.add_resource(UserResource, 'user/', defaults={"current_user": True}, 
                    endpoint='currentuser')
v1_api.add_resource(UserResource, 'users/', 'users/<int:id_>/')
v1_api.add_resource(LoginResource, 'login/')


app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["DATABASE_URL"]
app.db = SQLAlchemy(app)

login_manager = login.LoginManager()
login_manager.init_app(app)
app.secret_key = "\xa2P\x11\x94\xc7hW/e\xfft\x9b\x84^\x00\x8d@T\xbavW\x00\xf1\x97)\xdb\xec\xe1Q\xb1\xab;\x9eY\x145\xcd\xd7_K/\xac\xe0\x9dA\x97h0?\xbd\r\xd2\x11\xa0k\xb1\x9a\xb1\x942M\x10C\xec\xd6B\xce|\x89X\xd4\xb0\x90h\x12\xc0\xe6\xd1\xb1h\xc7\xaaI1r]*\xf7EV\n\xf7\x17\to3\xf8O\xfey@\xc7\xd2\x98g\x85|\xadLJ'>\x0f\xd7*X\x85r\xf0\x89\x006\x7f\x1cCu\xdf\xd3"


from auth import *

if __name__ == '__main__':
    app.run(debug=True)
