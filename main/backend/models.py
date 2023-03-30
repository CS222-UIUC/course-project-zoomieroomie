from . import app, db
from flask_bcrypt import Bcrypt
from flask_sqlalchemy import SQLAlchemy
from SQLAlchemy import Column, ForeignKey
from SQLAlchemy.orm import relationship, backref
bcrypt = Bcrypt(app)

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    preferences = relationship('Preferences', uselist=False, backref='user')

    def __repr__(self):
        return f'<User {self.username}>'
    
    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(
            password.encode('utf-8')
        )

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

class Preferences(db.Model):
    __tablename__ == 'preferences'
    id = db.Column(db.Integer, primary_key=True, ForeignKey('users.id'))
    l_smoker = db.Column(db.String(50))
    smoke = db.Column(db.String(50))
    l-drinker = db.Column(db.String(50))
    drink = db.Column(db.String(50))
    extrovert = db.Column(db.Integer)
    l-extrovert = db.Column(db.Integer)
    l-sexuality = db.Column(db.String(50))
    sexuality = db.Column(db.String(50))
    l-gender = db.Column(db.String(50))
    gender = db.Column(db.String(50))
    user = relationship('User', backref='preference')
