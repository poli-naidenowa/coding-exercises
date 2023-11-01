import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):
    # 1. Write a `fizzBuzz` method that accepts a number as input and returns it as a String.
    def test_is_input_is_number(self):

        number = FizzBuzz.readInput()
        result = number.isnumeric()
        expected = True

        self.assertEqual(result, expected)
        
if __name__ == '__main__': 
    unittest.main() 