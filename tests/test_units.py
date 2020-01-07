import unittest
from bbdata.endpoint import output


class TestUnits(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get(self):
        response = output.units.get()
        print(response)

    def test__post(self):
        # TODO Implement
        self.assertFalse(True)

    def tearDown(self) -> None:
        output.logout()
