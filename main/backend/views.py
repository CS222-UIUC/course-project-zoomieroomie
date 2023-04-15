"""Backend functionality for login, register, form submission"""
from flask import (
    request,
    session,
    redirect,
    url_for,
    flash,
    jsonify,
)
import bcrypt
import sqlalchemy as db

from . import app, db
from .models import User, Preferences

# from flask_cors import CORS

salt = bcrypt.gensalt()
engine = db.create_engine("sqlite:///database.sqlite")
metadata = db.MetaData()
connection = engine.connect()

# cors = CORS(
#     app, resources={r"*": {"origins": "*", "methods": "*", "allow_headers": "*"}}
# )

"""
def add_cors_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = 'Content-Type,Authorization'
    response.headers['Access-Control-Allow-Methods'] = 'GET,PUT,POST,DELETE,OPTIONS'
    return response

app.after_request(add_cors_headers)
"""


@app.route("/login", methods=["POST"])
def login():
    """Function that logs user in if user is in database"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and user.check_password(password):
        session["username"] = username
        return jsonify({"message": "Login successful!"}), 200
    return jsonify({"message": "Invalid username or password"}), 401


@app.route("/register", methods=["GET", "POST", "PUT", "DELETE"])
def register():
    """Function that registers nnew user into database"""
    print(request.json)
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    firstname = data.get("firstname")
    lastname = data.get("lastname")
    password_hash = bcrypt.hashpw(password, salt)

    with app.app_context():
        db.create_all()
        user = User(
            username=username,
            password=password_hash,
            firstname=firstname,
            lastname=lastname,
        )
        db.session.add(user)
        db.session.commit()
    return jsonify({"message": "User created successfully!"})


@app.route("/submit-form", methods=["POST"])
def submit_form():
    """Function that receives information from form"""
    if "username" in session:
        data = request.get_json()

        with app.app_context():
            pref = Preferences()
            pref.l_smoke = data["l-smoke"]
            pref.smoke = data["smoke"]
            pref.l_drink = data["l-drink"]
            pref.drink = data["drink"]
            pref.extrovert = data["extrovert"]
            pref.l_extrovert = data["l-extrovert"]
            pref.study = data["study"]
            pref.sleep = data["sleep"]
            pref.bedtime_school = data["bedtime-school"]
            pref.bedtime_weekend = data["bedtime-weekend"]
            pref.messy = data["messy"]
            pref.l_messy = data["l-messy"]
            pref.guests = data["guests"]
            pref.l_sexuality = data["l-sexuality"]
            pref.sexuality = data["sexuality"]
            pref.l_gender = data["l-gender"]
            pref.gender = data["gender"]

            db.session.add(pref)
            db.session.commit()

        response_data = {"success": True}
        flash("We have received your responses", "success")
        return jsonify(response_data)
    flash("Please log in to save your responses", "error")
    return redirect(url_for("login"))


@app.route("/preferences", methods=["GET"])
def get_preferences():
    """Function that returns list of all users that have inputted preferences"""
    preferences = Preferences.query.all()
    p_list = []
    for preference in preferences:
        p_list.append({"user": preference.user})
    return jsonify({"preferences": p_list})


@app.route("/users", methods=["GET"])
def get_users():
    """Function that returns all current users in database"""
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({"username": user.username})
    return jsonify({"users": user_list})


## DELETES ALL USERS FROM DATABASE!! DO NOT RUN!!(testing purposes only)
@app.route("/delete_all_users")
def delete_all_users():
    """Function that deletes all users from database"""
    User.query.delete()
    db.session.commit()
    return "All users have been deleted from the database"


@app.route("/api/test", methods=["GET"])
def test_route():
    """Test functionality"""
    return jsonify({"message": "Test route working"})
