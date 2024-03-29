from flask.ext import login, security

from .core import db

# schedules = db.Table('schedules',
#     db.Column('class_id', db.Integer, db.ForeignKey('class.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id'))
# )

# friend_lists = db.Table('friend_lists',
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
#     db.Column('user_id', db.Integer, db.ForeignKey('user.id')))

class Class(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(64))
    name = db.Column(db.String(128), index=True)
    number = db.Column(db.Integer, index=True)
    section = db.Column(db.Integer)

class User(db.Model, security.UserMixin):
    __tablename__ = 'workspaces_user'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(255))
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    first_name = db.Column(db.String(64), index=True)
    last_name = db.Column(db.String(64), index=True)

    # classes = db.relationship('Schedule', secondary=schedules,
    #     backref=db.backref('users', lazy='dynamic'))
    # friend_list = db.relationship('Friend_list', secondary=friend_lists,
    #     backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % (self.name)

class Role(db.Model, security.RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
