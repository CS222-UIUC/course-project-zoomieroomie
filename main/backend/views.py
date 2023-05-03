"""Backend functionality for login, register, form submission"""
from flask import request, session, redirect, url_for, flash, jsonify, render_template
import bcrypt
import sqlalchemy as db
from backend.__init__ import app, db
from .person import Person
from .models import User, Preferences

salt = bcrypt.gensalt()
engine = db.create_engine("sqlite:///database.sqlite")
metadata = db.MetaData()
connection = engine.connect()

person_dict = {}


@app.route("/login", methods=["POST"], endpoint="login")
def login():
    """Function that logs user in if user is in database"""
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    user = User.query.filter_by(email=email).first()
    if user and user.check_password(password):
        session["email"] = email
        return jsonify({"success": True}, 200)
    return jsonify({"success": False}, 400)


@app.route("/register", methods=["GET", "POST", "PUT", "DELETE"], endpoint="register")
def register():
    """Function that registers new user into database"""
    data = request.get_json()
    password = data.get("password")
    password_hash = bcrypt.hashpw(password, salt)

    with app.app_context():
        db.create_all()
        user = User(
            email=data["email"],
            password=password_hash,
            firstname=data["firstname"],
            lastname=data["lastname"],
        )
        db.session.add(user)
        db.session.commit()

    person = Person([email, password, firstname, lastname], [""], [""])
    person_dict[email] = person
    return jsonify({"success": True}, 200)


@app.route("/matches", methods=["GET"], endpoint="matches")
def matches():
    """Function that finds best roommate to be displayed on matches page"""
    if "email" in session:
        email = session["email"]
        person = person_dict[email]
        best_roommate = person.find_best(person_dict.values())
        flash("Best roommate found")
        return render_template("matches.tsx", best_roommate=best_roommate)

    flash("Please log in to see your roommate matches", "error")
    return redirect(url_for("login"))

@app.route("/main", methods=["GET"], endpoint="main")
def main():
    """Function that returns main page(dashboard) to user"""
    if "email" in session:
        return render_template("Main.tsx")
    flash("Please log in to see your dashboard", "error")
    return redirect(url_for("login"))


@app.route("/submit-form", methods=["POST"], endpoint="submit")
def submit_form():
    """Function that receives information from form"""
    if "email" in session:
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


@app.route("/preferences", methods=["GET"], endpoint="preferences")
def get_preferences():
    """Function that returns list of all users that have inputted preferences"""
    preferences = Preferences.query.all()
    p_list = []
    for preference in preferences:
        p_list.append({"user": preference.user})
    return jsonify({"preferences": p_list})


@app.route("/users", methods=["GET"], endpoint="users")
def get_users():
    """Function that returns all current users in database"""
    users = User.query.all()
    user_list = []
    for user in users:
        user_list.append({"email": user.email})
    return jsonify({"users": user_list})


## DELETES ALL USERS FROM DATABASE!! DO NOT RUN!!(testing purposes only)
@app.route("/delete_all_users", endpoint="delete")
def delete_all_users():
    """Function that deletes all users from database"""
    User.query.delete()
    db.session.commit()
    return "All users have been deleted from the database"


@app.route("/api/test", methods=["GET"], endpoint="test")
def test_route():
    """Test functionality"""
    return jsonify({"message": "Test route working"})
