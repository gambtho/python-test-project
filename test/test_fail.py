import unittest


class FailingTest(unittest.TestCase):
    def test_should_fail(self):
        self.assertTrue(False)
