from sqlalchemy.ext.declarative import declared_attr
from flask.ext.sqlalchemy import SQLAlchemy
from coaster import sqlalchemy

db = SQLAlchemy()

class BaseMixin(sqlalchemy.BaseMixin):
    
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()