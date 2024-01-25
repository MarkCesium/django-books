from django.test import TestCase
from store.logic import operations


# Create your tests here.
class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(2, 2, "+")
        self.assertAlmostEquals(4, result)

    def test_minus(self):
        result = operations(4, 2, "-")
        self.assertAlmostEquals(2, result)

    def test_multiply(self):
        result = operations(3, 3, "*")
        self.assertAlmostEquals(9, result)
