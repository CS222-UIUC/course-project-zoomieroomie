"""Unit tests for the matches page"""

import unittest
import re
from .person import Person
from .views import app


class TestMatches(unittest.TestCase):
    """Testing the matches page"""

    def setUp(self):
        """Setting up the people"""
        app.config["TESTING"] = True
        self.app = app.test_client()
        self.person_dict = {
            "john@example.com": Person(
                ["john@example.com", "password", "John", "Doe"], [""], [""]
            ),
            "jane@example.com": Person(
                ["jane@example.com", "password", "Jane", "Smith"], [""], [""]
            ),
            "jack@example.com": Person(
                ["jack@example.com", "password", "Jack", "Todd"], [""], [""]
            ),
            "jill@example.com": Person(
                ["jill@example.com", "password", "Jill", "Rick"], [""], [""]
            ),
        }
        self.app.secret_key = "secret"

    def tearDown(self):
        pass

    def test_matches_with_email_in_session(self):
        """Testing with user logged in"""
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "john@example.com"
            response = client.get("/matches")
            self.assertEqual(response.status_code, 200)
            self.assertTrue(
                re.search("Best roommate found", response.get_data(as_text=True))
            )

    def test_matches_with_no_email_in_session(self):
        """Testing without user logged in"""
        with self.app as client:
            response = client.get("/matches")
            self.assertEqual(response.status_code, 302)
            self.assertTrue(
                re.search(
                    "Please log in to see your roommate matches",
                    response.get_data(as_text=True),
                )
            )

    def test_matches_with_no_best_roommate(self):
        """Testing no matches"""
        with self.app as client:
            with client.session_transaction() as sess:
                sess["email"] = "jack@example.com"
            response = client.get("/matches")
            self.assertEqual(response.status_code, 200)
            self.assertIn(b"No matches found.", response.data)
