import unittest
from bbdata import output


class TestAuth(unittest.TestCase):

    def test__login(self):
        before_login = output.me.get()
        output.login()
        after_login = output.me.get()
        print(after_login)
        self.assertNotEqual(before_login, after_login, "User is logged out, he should be logged in")

    def test__logout(self):
        expected_exception = "AccessDenied"
        output.login()
        output.logout()
        response = output.me.get()
        print(response)
        exception = response["exception"]
        self.assertEqual(expected_exception, exception, "Exception AccessDenied wasn't thrown")
