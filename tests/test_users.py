import unittest
from bbdata import output


class TestUsers(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get(self):
        response = output.users.get()
        print(response)

    def tearDown(self) -> None:
        output.logout()
