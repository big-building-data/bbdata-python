import unittest
from bbdata import output


class TestComments(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get_all(self):
        response = output.comments.get_all()
        print(type(response))

    def test__put(self):
        return False

    def test__get(self):
        return False

    def test__delete(self):
        return False

    def test__post(self):
        return False

    def tearDown(self) -> None:
        output.logout()