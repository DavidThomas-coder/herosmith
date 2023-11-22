# backend/app.py
from flask import Flask
from models.user import db as user_db
from models.character import db as character_db

app = Flask(__name__)

# Replace the following URI with your PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://davidthomas@localhost/herosmith_development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the databases
user_db.init_app(app)
character_db.init_app(app)

# Create tables
with app.app_context():
    user_db.create_all()
    character_db.create_all()

# Rest of your app code...




