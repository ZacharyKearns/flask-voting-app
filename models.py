from flask_sqlalchemy import SQLAlchemy
from werkzeug import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'
    uid = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    pwdhash = db.Column(db.String(30))
    user = db.relationship('Poll', backref='user')

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pwdhash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.pwdhash, password)

class Poll(db.Model):
    __tablename__ = 'polls'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.Text())
    options = db.Column(db.Text())
    user_id = db.Column(db.Integer, db.ForeignKey('users.uid'))

    def __init__(self, name, options, user_id):
        self.name = name
        self.options = options
        self.user_id = user_id
