import CamelCase
import unittest

def count_signs_counts_correctly(self):
    data = "My-Awsome_project"
    result = CamelCase.countSigns(data)
    self.assertEqual(result, 2)
