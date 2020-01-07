import unittest
from bbdata.endpoint import output


class TestInfo(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get(self):
        response = output.values.get(
            2649,
            "2018-06-02T19:00",
            "2018-06-02T22:00",)
        print(response)

    def test__get_latest(self):
        response = output.values.get_latest(
            2649,
            "2018-06-02T19:00")
        print(response)

    def test__get_hours(self):
        response = output.values.get_hours(
            2649,
            "2018-06-02T19:00",
            "2018-06-02T22:00",)
        print(response)

    def test__get_quarters(self):
        response = output.values.get_quarters(
            2649,
            "2018-06-02T19:00",
            "2018-06-02T22:00",)
        print(response)

    def tearDown(self) -> None:
        output.logout()