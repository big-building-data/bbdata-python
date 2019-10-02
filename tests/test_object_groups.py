import unittest
from bbdata import output


class TestObjectGroups(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get_all(self):
        response = output.object_groups.get_all()
        print(response)

    def test__put(self):
        # TODO Implement test
        self.assertFalse(True)

    def test__get(self):
        response = output.object_groups.get(3)
        print(response)

    def test__post(self):
        # TODO Implement test
        #response = output.object_groups.post()
        self.assertFalse(True)

    def test__delete(self):
        # TODO Implement test
        #response = output.object_groups.delete()
        self.assertFalse(True)

    def test__get_object(self):
        response = output.object_groups.get_objects(3)
        print(response)

    def test__put_object(self):
        # TODO Implement test
        #response = output.object_groups.put_object(3, 2648)
        self.assertFalse(True)

    def test__delete_object(self):
        # TODO Implement test
        #response = output.object_groups.delete_object(3, 2648)
        self.assertFalse(True)

    def test__get_permissions(self):
        response = output.object_groups.get_permissions(3)
        print(response)

    def test__put_permissions(self):
        # TODO Implement test
        #response = output.object_groups.put_permissions(3, 4)
        self.assertFalse(True)

    def test__delete_permissions(self):
        # TODO Implement test
        #response = output.object_groups.delete_permissions(3, 4)
        self.assertFalse(True)

    def tearDown(self) -> None:
        output.logout()
