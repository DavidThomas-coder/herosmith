# backend/models/models.py
from datetime import datetime
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)

    characters = db.relationship('Character', backref='user', lazy=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

class Character(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(80), nullable=False)
    char_class = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    background = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __init__(self, race, char_class, name, background):
        self.race = race
        self.char_class = char_class
        self.name = name
        self.background = background
