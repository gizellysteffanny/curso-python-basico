from unittest import TestCase


def hello_world():
    return 'Hello World'


class HelloWorldTestCase(TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_hello_world(self):
        result = hello_world()
        self.assertEqual(result, 'Hello World')
