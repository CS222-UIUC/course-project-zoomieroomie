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
from .models import User, Preferences
from flask_bcrypt import Bcrypt
from flask_cors import CORS

bcrypt = Bcrypt(app)

#cors = CORS(app, resources={r"*": {"origins": "*", "methods": "*", "allow_headers": "*"}})

'''
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

app.after_request(add_cors_headers)
'''

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

@app.route('/register', methods=['GET', 'POST', 'PUT', 'DELETE'])
def register():
    print(request.json)
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    firstname = data.get('firstname')
    lastname = data.get('lastname')
    password_hash = bcrypt.generate_password_hash(password.encode('utf-8'))


    with app.app_context():
        db.create_all()
        user = User(username=username, password=password_hash, firstname=firstname, lastname=lastname)
        db.session.add(user)
        db.session.commit()
    return jsonify({'message': 'User created successfully!'})

@app.route('/submit-form', methods=['POST'])
def submit_form():
    """Function that received information from form"""
    if "username" in session:
        data = request.get_json()
        l_smoker = data.get('l-smoker')

        with app.app_context():
            preferences = Preferences(l_smoker=l_smoker)
            db.session.add(preferences)
            db.session.commit()

        response_data = {"status": "success"}
        flash("We have received your responses", "success")
        return jsonify(response_data)
    flash("Please log in to save your responses", "error")
    return redirect(url_for("login"))

@app.route('/preferences', methods=['GET'])
def get_preferences():
    preferences = Preferences.query.all()
    p_list = []
    for preference in preferences:
        p_list.append({'user': preference.user})
    return jsonify({'preferences': p_list})

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

@app.route('/api/test', methods=['GET'])
def test_route():
    return jsonify({'message': 'Test route working'})