import unittest
from bbdata import output


class TestTypes(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get(self):
        response = output.types.get()
        print(response)

    def tearDown(self) -> None:
        output.logout()
