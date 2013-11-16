from ..core import db, BaseMixin


class Location(BaseMixin, db.Model):
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    name = db.Column(db.Text)
    reference = db.Column(db.String(256), unique=True)
    posts = db.relationship('Post', backref='location', lazy='dynamic')
    
class Post(BaseMixin, db.Model):
    message = db.Column(db.Text)
    class_id = db.Column(db.Integer, db.ForeignKey('class.id'))
    creator_id = db.Column(db.Integer, db.ForeignKey('workspaces_user.id'), 
        nullable=False)
    location_id = db.Column(db.Integer, db.ForeignKey('location.id'))