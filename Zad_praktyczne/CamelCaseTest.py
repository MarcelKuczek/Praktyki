import CamelCase
import unittest

class TestOperations(unittest.TestCase):
    def test_add(self):
        data = "My-Awsome_project"
        result = CamelCase.countSigns(data)
        self.assertEqual(result, 2)

if __name__ == '__main__':
    unittest.main()
