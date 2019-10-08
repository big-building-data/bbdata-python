import unittest
from bbdata import output


class TestComments(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get_all(self):
        response = output.comments.get_all()
        print(response)

    def test__put(self):
        # response = output.comments.put(...)
        self.assertFalse(True)

    def test__get(self):
        response = output.comments.get(1)
        print(response)

    def test__delete(self):
        # response = output.comments.delete(...)
        self.assertFalse(True)

    def test__post(self):
        # response = output.comments.post(...)
        self.assertFalse(True)

    def tearDown(self) -> None:
        output.logout()