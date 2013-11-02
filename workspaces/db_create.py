from api import app
from models import *

db = app.db

db.create_all()