"""Database models for ZoomieRoomie"""
import bcrypt
from SQLAlchemy import ForeignKey
from SQLAlchemy.orm import relationship
from . import db

salt = bcrypt.gensalt()
# bcrypt = Bcrypt(app)


class User(db.Model):
    """User table in database"""

    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)
    firstname = db.Column(db.String(50), nullable=False)
    lastname = db.Column(db.String(50), nullable=False)
    preferences = relationship("Preferences", uselist=False, backref="user")

    def __repr__(self):
        """Defines string representation"""
        return f"<User {self.username}>"

    def set_password(self, password):
        """Sets user password"""
        self.password = bcrypt.hashpw(password, salt)

    def check_password(self, password):
        """Compares password with hash"""
        hash_p = bcrypt.hashpw(password, salt)
        return hash_p == self.password


class Preferences(db.Model):
    """Preferences table in database (one-to-one with Users)"""

    __tablename__ = "preferences"
    id = db.Column(db.Integer, ForeignKey("users.id"), primary_key=True)
    l_smoke = db.Column(db.Integer())
    smoke = db.Column(db.Integer())
    l_drink = db.Column(db.Integer())
    drink = db.Column(db.Integer())
    extrovert = db.Column(db.Integer())
    l_extrovert = db.Column(db.Integer())
    l_sexuality = db.Column(db.Integer())
    sexuality = db.Column(db.Integer())
    l_gender = db.Column(db.Integer())
    gender = db.Column(db.Integer())
    user = relationship("User", backref="preference")

    def __repr__(self):
        """Defines string representation"""
        return f"<Preferences for {self.user}>"

    def get_user(self):
        """Returns user who owns preferences"""
        return self.user
