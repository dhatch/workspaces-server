from flask import Flask
from flask.ext import restful

app = Flask(__name__)
api = restful.Api(app)
app.db = SQLAlchemy(app)

if __name__ == '__main__':
    app.run(debug=True)