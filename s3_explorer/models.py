from flask_login import UserMixin
from s3_explorer import db


class User(UserMixin, db.Model):
    __tablename__ = "user"
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(2000))
    
    
class Account(UserMixin, db.Model):
    __tablename__ = "account"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    endpoint = db.Column(db.String(200))
    access_key_id = db.Column(db.String(200))
    secret_access_key = db.Column(db.String(200))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
