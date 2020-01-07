import unittest
from bbdata.endpoint import output


class TestUserGroups(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get_all(self):
        response = output.user_groups.get_all()
        print(response)

    def test__put(self):
        name_too_short = "aa"
        name_too_long = "aaaaaaaaaaaaaaaaaaaaaaaaa" \
                        + "aaaaaaaaaaaaaaaaaaaaaaaaa" \
                        + "a"
        with self.assertRaises(ValueError):
            output.user_groups.put(name_too_short)
            output.user_groups.put(name_too_long)

    def test__delete(self):
        # TODO Implement test
        # response = output.user_groups.put(name)
        self.assertFalse(True)

    def test__get(self):
        response = output.user_groups.get(4)
        print(response)

    def test__get_users(self):
        response = output.user_groups.get_users(4)
        print(response)

    def test__put_users(self):
        # response = output.user_groups.put_users(...)
        # print(response)
        self.assertFalse(True)

    def test__delete_users(self):
        # TODO Implement test
        # response = output.user_groups.delete_users(name)
        self.assertFalse(True)

    def test__put_users_new(self):
        # TODO Implement test
        # response = output.user_groups.put_users_new(...)
        self.assertFalse(True)

    def tearDown(self) -> None:
        output.logout()
