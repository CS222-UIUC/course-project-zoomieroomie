from flask import (
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash,
    jsonify,
    make_response,
)
from . import app, db
from .models import User
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt(app)

@app.route("/")
def hello_world():
    return 'Hello, World!'

@app.route("/login", methods=['POST'])
def login():
    """Function that logs user in if user is in database"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session['username'] = username
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401

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