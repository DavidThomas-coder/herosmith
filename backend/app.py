# backend/app.py
from flask import Flask
from models.user import db as user_db
from models.character import db as character_db

app = Flask(__name__)

# Configure the database URI, e.g., PostgreSQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://username:password@localhost/mydatabase'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize the databases
user_db.init_app(app)
character_db.init_app(app)

# Create tables
with app.app_context():
    user_db.create_all()
    character_db.create_all()

# Rest of your app code...



