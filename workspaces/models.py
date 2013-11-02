from workspaces.api import app

db = app.db

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

class User(db.Model):
    __tablename__ = 'workspaces_user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    # classes = db.relationship('Schedule', secondary=schedules,
    #     backref=db.backref('users', lazy='dynamic'))
    # friend_list = db.relationship('Friend_list', secondary=friend_lists,
    #     backref=db.backref('users', lazy='dynamic'))

    def __repr__(self):
        return '<User %r>' % (self.name)