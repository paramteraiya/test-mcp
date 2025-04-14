import unittest
from add_numbers import add_two_numbers

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add_two_numbers(5, 10), 15)
        
    def test_add_negative_numbers(self):
        self.assertEqual(add_two_numbers(-3, -7), -10)
        
    def test_add_mixed_numbers(self):
        self.assertEqual(add_two_numbers(-5, 10), 5)
        
    def test_add_zero(self):
        self.assertEqual(add_two_numbers(0, 10), 10)
        self.assertEqual(add_two_numbers(10, 0), 10)
        
if __name__ == "__main__":
    unittest.main()