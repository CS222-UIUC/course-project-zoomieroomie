# app.py
#REGISTER_BACKEND

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}}, methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Access-Control-Allow-Origin"])

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'


@app.route('/register', methods=['POST'])
def register():
    print(request.json)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))


    with app.app_context():
        db.create_all()
        user = User(username=username, password=password_hash)
        db.session.add(user)
        db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({'username': user.username})
    return jsonify({'users': user_list})

## DELETES ALL USERS FROM DATABASE!! DO NOT RUN!!(testing purposes only)
@app.route('/delete_all_users')
def delete_all_users():
    User.query.delete()
    db.session.commit()
    return "All users have been deleted from the database"