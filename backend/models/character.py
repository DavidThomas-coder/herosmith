# backend/models/character.py
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from models.user import User

db = SQLAlchemy()

class Character(db.Model):
    __tablename__ = 'character'
    id = db.Column(db.Integer, primary_key=True)
    race = db.Column(db.String(80), nullable=False)
    char_class = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    background = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id', name='fk_user_id'))

    def __init__(self, race, char_class, name, background):
        self.race = race
        self.char_class = char_class
        self.name = name
        self.background = background

