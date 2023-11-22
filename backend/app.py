# backend/app.py
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from models.user import User
from models.character import Character

app = Flask(__name__)

# Replace the following URI with your PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://davidthomas@localhost/herosmith_development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the SQLAlchemy instance
db = SQLAlchemy(app)

# Create tables
with app.app_context():
    db.create_all()

# Rest of your app code...





