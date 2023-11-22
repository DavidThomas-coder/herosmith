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

# Root route
@app.route('/')
def index():
    return 'Hello, Flask!'

# Rest of your app code...

if __name__ == '__main__':
    app.run(debug=True)
