#!/usr/bin/env python3

def greet_programmer():
    print("Hello, programmer!")

def greet(name):
    print(f"Hello, {name}!")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Call the function with an argument to see the output
greet("Naureen")

def greet_with_default(name="programmer"):
    print(f"Hello, {name}!")

# Call the function with no arguments to see the default output
greet_with_default()

# Call the function with an argument to see the custom output
greet_with_default("Sunny")

# Function to add two numbers
def add(num1, num2):
    return num1 + num2

# Example usage
sum = add(1, 2)
print(sum)  # Output: 3

# Function to halve a number, returning None if the input is not a number
def halve(number):
    if not isinstance(number, (int, float)):
        return None
    return number / 2

# Example usage
result = halve(4)
print(result)  # Output: 2

result = halve("two")
print(result)  # Output: None
