# 1. Write a `fizzBuzz` method that accepts a number as input and returns it as a String.
# 2. For multiples of three return “Fizz” instead of the number
# 3. For the multiples of five return “Buzz”
# 4. For numbers that are multiples of both three and five return “FizzBuzz”.

def fizzBuzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    elif number % 3 == 0:
        return "Fizz"
    elif number % 5 == 0:
        return "Buzz"

text = input("Enter your number: ")

while text != "End":

    print(fizzBuzz(int(text)))
    text = input("Enter your number or End to exit of the program: ")


