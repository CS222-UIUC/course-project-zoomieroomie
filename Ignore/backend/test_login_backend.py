"""Unit tests for the login backend"""
import unittest
import tempfile
import os
import sqlite3
import re
from login_backend import app


class FlaskTestCase(unittest.TestCase):
    """Testing the login class with Flask"""

    def setUp(self):
        app.config["TESTING"] = True
        self.app = app.test_client()
        with tempfile.NamedTemporaryFile(delete=False) as temp_db:
            app.config["DATABASE"] = temp_db.name

            # with app.app_context():
            #     with app.test_client() as c:
            #         with app.open_resource('users.sql', mode='r') as f:
            conn = sqlite3.connect("users.sql")
            cursor = conn.cursor()
            cursor.execute(
                """DELETE FROM users WHERE username=? AND password=?""",
                ("test", "test"),
            )
            cursor.execute(
                """INSERT INTO users (username, password) VALUES (?, ?)""",
                ("test", "test"),
            )
            conn.commit()

    def tearDown(self):
        os.unlink(app.config["DATABASE"])

    def test_login_success(self):
        """Testing login success with existing user"""
        response = self.app.post(
            "/", data=dict(username="test", password="test"), follow_redirects=True
        )
        # self.assertIn(b'Welcome test!', response.data)
        self.assertTrue(re.search("Welcome test!", response.get_data(as_text=True)))

    def test_login_invalid_username(self):
        """Testing login fail with invalid username"""
        response = self.app.post(
            "/", data=dict(username="invalid", password="test"), follow_redirects=True
        )
        # self.assertIn(b'Invalid username or password', response.data)
        self.assertTrue(
            re.search("Invalid username or password", response.get_data(as_text=True))
        )

    def test_login_invalid_password(self):
        """Testing login fail with incorrect password"""
        response = self.app.post(
            "/", data=dict(username="test", password="invalid"), follow_redirects=True
        )
        # self.assertIn(b'Invalid username or password', response.data)
        self.assertTrue(
            re.search("Invalid username or password", response.get_data(as_text=True))
        )

    def test_dashboard_authenticated(self):
        """Testing dashboard success with valid user"""
        with self.app.session_transaction() as session:
            session["username"] = "test"
        response = self.app.get("/dashboard", follow_redirects=True)
        # self.assertIn(b'Welcome test!', response.data)
        self.assertTrue(re.search("Welcome test!", response.get_data(as_text=True)))

    def test_dashboard_unauthenticated(self):
        """Testing dashboard fail with invalid user"""
        response = self.app.get("/dashboard", follow_redirects=True)
        # self.assertIn(b'Please log in to access this page', response.data)
        self.assertTrue(
            re.search(
                "Please log in to access this page", response.get_data(as_text=True)
            )
        )

    def test_logout(self):
        """Testing session logout"""
        with self.app.session_transaction() as session:
            session["username"] = "test"
        response = self.app.get("/logout", follow_redirects=True)
        # self.assertIn(b'You have been logged out', response.data)
        self.assertTrue(
            re.search("You have been logged out", response.get_data(as_text=True))
        )


if __name__ == "__main__":
    unittest.main()
