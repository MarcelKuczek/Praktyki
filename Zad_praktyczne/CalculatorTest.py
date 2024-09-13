import Calculator
import unittest

class TestOperation(unittest.TestCase):

    def test_add(self):
        result = 2
        i = 1
        operation = ['2', '+', '3']
        operation = list(operation)
        result = Calculator.add(result, i, operation)
        self.assertEqual(result, 5)