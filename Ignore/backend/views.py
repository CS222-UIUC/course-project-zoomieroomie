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
from app import app, db
from models import User
from flask_bcrypt import Bcrypt


bcrypt = Bcrypt(app)

@app.route("/login", methods=['POST', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Origin', '*')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        return response

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

@app.route('/register', methods=['POST', 'OPTIONS'])
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
