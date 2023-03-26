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

app = Flask(__name__)
app.secret_key = "secret_key"  # set secret_key


@app.route("/", methods=["GET", "POST"])
def login():
    """Function that logs user in if user is in database"""
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        # check if user exists in database
        conn = sqlite3.connect("users.sql")
        cursor = conn.cursor()
        cursor.execute(
            """SELECT * FROM users WHERE username=? AND password=?""",
            (username, password),
        )
        user = cursor.fetchone()
        conn.close()

        if user:
            # set session variable for current user
            session["username"] = user[1]
            flash(f"Welcome {user[1]}!", "success")
            return redirect(url_for("dashboard"))
        flash("Invalid username or password", "error")
    return render_template("login.html")


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
    app.run(debug=True)
