from ..core import db

department_classes = db.Table('departments_classes',
    db.Column('department_id', db.Integer, db.ForeignKey('department.id')),
    db.Column('class_id', db.Integer, db.ForeignKey('class.id'))
)

class Department(db.Model):
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    abbreviation = db.Column(db.String(10), index=True, nullable=False)
    classes = db.relationship('Class', secondary=departments_classes,
        backref=db.backref('departments'), lazy='dynamic')
    
class Class(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    department = db.Column(db.String(64))
    name = db.Column(db.String(255), index=True, nullable=False)
    number = db.Column(db.Integer, index=True, nullable=False)
    section = db.Column(db.Integer)