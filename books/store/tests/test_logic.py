from store.logic import operations
from django.test import TestCase


class LogicTestCase(TestCase):
    def test_plus(self):
        result = operations(4, 6, '+')
        self.assertEqual(10, result)

    def test_minus(self):
        result = operations(10, 6, '-')
        self.assertEqual(4, result)

    def test_multiply(self):
        result = operations(2, 6, '*')
        self.assertEqual(12, result)
