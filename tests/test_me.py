import unittest
from bbdata import output


class TestMe(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get(self):
        response = output.me.get()
        print(response)

    def test__get_groups(self):
        response = output.me.get_groups()
        print(response)

    def test__get_apikeys(self):
        response = output.me.get_apikeys()
        print(response)

    def test__put_apikeys(self):
        # TODO Implement test
        # response = output.me.put_apikeys(...)
        self.assertFalse(True)

    def test__post_apikeys(self):
        # TODO Implement test
        # response = output.me.post_apikeys(...)
        self.assertFalse(True)

    def test__delete_apikeys(self):
        # TODO Implement test
        # response = output.me.put_apikeys(...)
        self.assertFalse(True)

    def tearDown(self) -> None:
        output.logout()
