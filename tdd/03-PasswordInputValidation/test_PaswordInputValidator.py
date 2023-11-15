"""
Create a function that can be used as a validator for the password field of a user registration form.
The validation function takes a string as an input and returns a validation result.
The validation result should contain a boolean indicating if the password is valid or not,
and also a field with the possible validation errors.

**Requirements**

1. The password must be at least 8 characters long.
   If it is not met, then the following error message should be returned:
   “Password must be at least 8 characters”
2. The password must contain at least 2 numbers.
   If it is not met, then the following error message should be returned:
   “The password must contain at least 2 numbers”
3. The validation function should handle multiple validation errors.
    - For example, “somepassword” should an error message:
      “Password must be at least 8 characters\nThe password must contain at least 2 numbers”
4. The password must contain at least one capital letter.
   If it is not met, then the following error message should be returned:
   “password must contain at least one capital letter”
5. The password must contain at least one special character.
   If it is not met, then the following error message should be returned:
   “password must contain at least one special character”

"""

import unittest

import PasswordValidator

class TestPaswordValidaro(unittest.TestCase):

    def test_multiple_validation_errors(self):
        """
        3. The validation function should handle multiple validation errors.
        - For example, “somepassword” should an error message:
         “Password must be at least 8 characters\nThe password must contain at least 2 numbers”

        """
        expected = "Password must be at least 8 characters\nThe password must contain at least 2 numbers"
        result = PasswordValidator.passwordValidator("poli")

        self.assertEqual(expected, result)

    def test_length_of_password(self):
        """
        1. The password must be at least 8 characters long.
         If it is not met, then the following error message should be returned:
        “Password must be at least 8 characters”
        """
        expected = "Password must be at least 8 characters"
        result = PasswordValidator.passwordValidator("poli123")

        self.assertEqual(expected, result)

    def test_is_two_numbers_in_password(self):
        """
        2. The password must contain at least 2 numbers.
         If it is not met, then the following error message should be returned:
        “The password must contain at least 2 numbers”
        """
        expected = "The password must contain at least 2 numbers"
        result = PasswordValidator.passwordValidator("polipoli")

        self.assertEqual(expected, result)


    def test_contains_capitals(self):
        """
        4. The password must contain at least one capital letter.
        If it is not met, then the following error message should be returned:
        “password must contain at least one capital letter”
        """
        expected = "password must contain at least one capital letter"
        result = PasswordValidator.passwordValidator("polipol112")

    def test_contains_special_simbols(self):
        """
        5. The password must contain at least one special character.
        If it is not met, then the following error message should be returned:
        “password must contain at least one special character”
        """
        expected = "password must contain at least one special character"
        result = PasswordValidator.passwordValidator("Paulina1234")

        self.assertEqual(expected, result)

    

if __name__ == '__main__': 
    unittest.main() 