from flask import Flask, request, jsonify
from flask_login import LoginManager, login_user, logout_user, login_required, current_user
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from models.user import User
from models.character import Character

from flask_cors import CORS

app = Flask(__name__)

# Enable CORS for all routes
CORS(app)

# Replace the following URI with your PostgreSQL database URI
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://davidthomas@localhost/herosmith_development'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'your_secret_key'  # Add a secret key for session management

# Print the database URI
print("Database URI:", app.config['SQLALCHEMY_DATABASE_URI'])

# Initialize the SQLAlchemy instance and run migration
db = SQLAlchemy(app)
migrate = Migrate(app, db)

login_manager = LoginManager(app)
login_manager.login_view = 'login'  # Specify the login view

# Create tables
with app.app_context():
    db.create_all()
    inspector = db.inspect(db.engine)
    print("Tables created:", inspector.get_table_names())

# Root route
@app.route('/')
def index():
    return 'Hello, I am Flask'

# API endpoint for user registration
@app.route('/api/register', methods=['POST'])
def register():
    try:
        data = request.json
        new_user = User(username=data['username'], password=data['password'], email=data.get('email'))
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User registered successfully'})
    except Exception as e:
        print('Error during user registration:', str(e))
        return jsonify({'message': 'Error registering user', 'error': str(e)}), 500


# API endpoint for user login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json

    user = User.query.filter_by(username=data['username']).first()

    if user and user.password == data['password']:
        login_user(user)
        return jsonify({'message': 'Login successful'})

    return jsonify({'message': 'Invalid username or password'}), 401

# API endpoint for user logout
@app.route('/api/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logout successful'})

if __name__ == '__main__':
    app.run(debug=True)
