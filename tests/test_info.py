import unittest
from bbdata.endpoint import output


class TestInfo(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get(self):
        response = output.info.get()
        print(response)

    def tearDown(self) -> None:
        output.logout()