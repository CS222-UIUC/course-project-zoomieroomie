"""Login Backend"""
import sqlite3
from flask import (
    Flask,
    render_template,
    request,
    session,
    redirect,
    url_for,
    flash,
    jsonify,
)
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#configuring the app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "http://localhost:3001"}}, methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Access-Control-Allow-Origin"])
#app.secret_key = "secret_key"  # set secret_key

#configuring the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

#configuring bcrypt (used for encrypting passwords)
bcrypt = Bcrypt(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<User {self.username}>'

@app.route("/login", methods=['POST'])
def login():
    """Function that logs user in if user is in database"""
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = User.query.filter_by(username=username).first()
    if user and bcrypt.check_password_hash(user.password, password):
        return jsonify({'message': 'Login successful!'}), 200
    else:
        return jsonify({'message': 'Invalid username or password'}), 401


@app.route("/dashboard")
def dashboard():
    """Function that takes user to dashboard if logged in"""
    if "username" in session:
        user = session["username"]
        flash(f"Welcome {user}!", "success")
        return render_template("dashboard.html", username=session["username"])
    flash("Please log in to access this page", "error")
    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    """Function that logs user out of current session"""
    session.pop("username", None)
    flash("You have been logged out", "success")
    return redirect(url_for("login"))


@app.route("/submit-form", methods=["POST"])
def submit_form():
    """Function that received information from form"""
    if "username" in session:
        data = request.get_json()
        response_data = {"status": "success"}
        flash("We have received your responses", "success")
        return jsonify(response_data)
    flash("Please log in to save your responses", "error")
    return redirect(url_for("login"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)
