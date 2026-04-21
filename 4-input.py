# Taking user input in Python

# In Python, we can take user input using the built-in function `input()`. The `input()` function reads a line from the input (usually from the user), converts it into a string, and returns it.

a = input("Please enter your name: ")
print("My name is ", a)


x = input("Enter first number: ")
y = input("Enter second number: ")
print("The sum of two numbers is: ", x + y)  # first number = 100, second number = 20, output: 10020

print("The sum of two integer numbers is: ", int(x) + int(y))  # first number = 100, second number = 20, output: 120

print("The sum of two float numbers is: ", float(x) + float(y))  # first number = 100, second number = 20, output: 120.0

print("The sum of two string is: ", str(x) + str(y))  # first number = 100, second number = 20, output: 10020

print("The sum of two boolean numbers is: ", bool(x) + bool(y))  # first number = 100, second number = 20, output: 2

print("The difference of two numbers is: ", int(x) - int(y))  # first number = 100, second number = 20, output: 80

print("The multiplication of two numbers is: ", float(x) * float(y))  # first number = 100, second number = 20, output: 2000.0

print("The floor division of two numbers is: ", float(x) // float(y))  # first number = 100, second number = 20, output: 5.0

print("The remainder of two numbers is: ", float(x) % float(y))  # first number = 100, second number = 20, output: 0.0

print("The power of two numbers is: ", int(x) ** int(y))  # first number = 100, second number = 2, output: 100 * 100 = 10000