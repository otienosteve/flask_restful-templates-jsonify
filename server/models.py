from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from flask_login import UserMixin

db = SQLAlchemy()

class Student(db.Model,SerializerMixin):
    __tablename__='student'
    # serialize_rules= ('-course')

    id=db.Column(db.Integer,primary_key=True)
    firstname=db.Column(db.String)
    lastname=db.Column(db.String)
    email=db.Column(db.String)
    gender=db.Column(db.String)
    feebalance=db.Column(db.Float)
    course = db.relationship('Units',backref='student')
    
    def __repr__(self):
        return  f"< User: {self.firstname} >"
    
class Units(db.Model,SerializerMixin):

    __tablename__ ='units'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    student_id = db.Column(db.Integer,db.ForeignKey('student.id'))

    def __repr__(self):
        return  f"< Unit: {self.name} >"
    
class User(db.Model,UserMixin):
    id= db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(40),nullable=False)
    email=db.Column(db.String(40),nullable=False)
    password = db.Column(db.String(200),nullable=False)

