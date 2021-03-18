import unittest 
from app.factorial import number_factorial
from app.divisible_by_7 import divisible_by_7
from app.number_multiple import generate_dict

class TestExercise(unittest.TestCase):
    def test_factorial_1(self):
        result = number_factorial(0)
        self.assertEqual(result, 1)
    
    def test_factorial_result_is_an_integer(self):
        result = number_factorial(45)
        self.assertIsInstance(result, int)
    
    def test_range_of_numbers_divisible_by_7(self):
        result = divisible_by_7()
        self.assertIsInstance(result, str)
    
    def test_generate_dict_returns_dict(self):
        result = generate_dict(1)
        self.assertIsInstance(result, dict)
    
    def test_generate_dict_returns_dict(self):
        result = generate_dict(2)
        self.assertEqual(result, {1:1, 2:4})