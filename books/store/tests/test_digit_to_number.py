from unittest import TestCase
from store.digit_to_number import *


class DigitToNumberTestCase(TestCase):
    def test_zero(self):
        result = number_digit(0)
        self.assertEqual(result, '0')

    def test_10(self):
        result = number_digit(10)
        self.assertEqual(result, '10')

    def test_22(self):
        result = number_digit(22)
        self.assertEqual(result, '20 + 2')

    def test_123123(self):
        result = number_digit(123123)
        self.assertEqual(result, '100000 + 20000 + 3000 + 100 + 20 + 3')

    def test_negative_number(self):
        with self.assertRaises(ValueError) as ex:
            result = number_digit(-5)
        self.assertEqual(ex.exception.args[0], 'Число должно быть положительным')