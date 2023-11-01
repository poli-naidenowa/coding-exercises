import unittest
import FizzBuzz


class TestFizzBuzz(unittest.TestCase):

    def test_is_input_is_number_gw(self):
        """ 
        1. Write a `fizzBuzz` method that accepts a 
        number as input and returns it as a String.
        """
        number = 2
        result = FizzBuzz.fizzBuzz(number)

        self.assertEqual(result, str(number))
    
    def test_is_Fizz(self):
        """
        2. For multiples of three return “Fizz” instead of the number
        """
        number = 3
        result = FizzBuzz.fizzBuzz(number)

        self.assertEqual(result, "Fizz")

    def test_is_Buzz(self):
        """
        3. For the multiples of five return “Buzz”
        """
        number = 5
        result = FizzBuzz.fizzBuzz(number)

        self.assertEqual(result, "Buzz")

    def test_is_FizzBuzz(self):
        """
        4. For numbers that are multiples of both three and five return “FizzBuzz”
        """
        number = 15
        result = FizzBuzz.fizzBuzz(number)

        self.assertEqual(result, "FizzBuzz")

if __name__ == '__main__': 
    unittest.main() 
