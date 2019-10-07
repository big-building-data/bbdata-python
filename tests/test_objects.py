import unittest
from bbdata import output


class TestInfo(unittest.TestCase):

    def setUp(self) -> None:
        output.login()

    def test__get_all(self):
        # TODO Implement test
        response = output.objects.get_all()
        print(response)

    def test__put(self):
        # TODO Implement test
        # response = output.objects.put(...)
        self.assertFalse(True)

    def test__get(self):
        # TODO Implement test
        response = output.objects.get(2648)
        print(response)

    def test__post(self):
        # TODO Implement test
        # response = output.objects.post(...)
        self.assertFalse(True)

    def test__delete(self):
        # TODO Implement test
        # response = output.objects.delete(...)
        self.assertFalse(True)

    def test__post_disable(self):
        # TODO Implement test
        # response = output.objects.post_disable(...)
        self.assertFalse(True)

    def test__post_enable(self):
        # TODO Implement test
        # response = output.objects.post_enable(...)
        self.assertFalse(True)

    def test__get_tokens(self):
        # TODO Implement test
        response = output.objects.get_tokens(2648, "A test")
        print(response)

    def test__put_tokens(self):
        # TODO Implement test
        # response = output.objects.put_tokens(...)
        self.assertFalse(True)

    def test__post_tokens(self):
        # TODO Implement test
        # response = output.objects.post_tokens(...)
        self.assertFalse(True)

    def test__delete_tokens(self):
        # TODO Implement test
        # response = output.objects.delete_tokens(...)
        self.assertFalse(True)

    def test__put_tags(self):
        # TODO Implement test
        # response = output.objects.put_tags(...)
        self.assertFalse(True)

    def test__delete_tags(self):
        # TODO Implement test
        # response = output.objects.delete_tags(...)
        self.assertFalse(True)

    def test__get_comments(self):
        # TODO Implement test
        response = output.objects.get_comments(2684)
        print(response)

    def tearDown(self) -> None:
        output.logout()
