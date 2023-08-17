#!/usr/bin/env python3


def admin_login(username, password):
    # your code here
    if (
        username.lower() == "admin"
        and username.upper() == "ADMIN"
        and password == "12345"
    ):
        return "Access granted"
    else:
        return "Access denied"


# def hows_the_weather(temperature):
#     # your code here
#     if temperature < 40:
#         response = "brisk"
#     elif 40 <= temperature <= 65:
#         response = "It's perfect out there!"
#     elif temperature > 85:
#         response = "too dang hot"
#     else:
#         response = "perfect"


#     return f"It's {response} out there!"
def hows_the_weather(temperature):
    if temperature < 40:
        response = "brisk"
    elif 40 <= temperature <= 65:
        response = "a little chilly"
    elif temperature > 85:
        response = "too dang hot"
    else:
        response = "perfect"

    return f"It's {response} out there!"


def fizzbuzz(num):
    # your code here
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num


# Write a method `calculator` that takes three arguments: an operation and two
#   numbers. If the operation is one of the following: `+`, `-`, `*`, or `\`,
#   return the value of calling the operation on the two numbers. Otherwise,
#   output a message saying "Invalid operation!" and return `nil`.
def calculator(operation, num1, num2):
    # your code here
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 != 0:
            return num1 / num2
        else:
            print("Division by zero is not allowed.")
            return None
    else:
        print("Invalid operation!")
