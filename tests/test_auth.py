import unittest
from bbdata.endpoint import output
from src.bbdata.exceptions import LoginRequiredException


class TestAuth(unittest.TestCase):

    def test__auth(self):
        with self.assertRaises(Exception):
            output.me.get()

    def test__login(self):
        try:
            output.login()
            me = output.me.get()
            print(me)
        except Exception:
            self.fail("User is logged out, he should be logged in")

    def test__logout(self):
        output.login()
        output.logout()
        with self.assertRaises(Exception):
            me = output.me.get()