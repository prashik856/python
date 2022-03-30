print("22. Functions")
# Code Reuse
# Don't Repeat yourself : DRY
# Don't be WET (We Enjoy Typing or Write Everything Twice)
# Any statement that consists of a word followed by information in parentheses is a function call.
# Examples
print("Hello World")
range(2, 20)
str(12)
range(10, 20, 3)
# The word in front of the parentheses are function names, and the comma-separated values inside the parentheses
# are function arguments
# create using def.
def my_func():
    print("spam")
    print("spam")
    print("spam")
my_func()
# Code block inside function should be intended.
# Define function before they can be called.
def hello():
    print("Hello World")
hello()


print("23. Function Arguments")
def printWithExclamation(word):
    print(word + "!")
printWithExclamation("spam")
printWithExclamation("eggs")
printWithExclamation("python")
# Argument is defined inside parentheses
# More than one argument
def printSumTwice(x, y):
    print(x + y)
    print(x + y)
printSumTwice(5, 8)
# Function arguments can be used inside function as variables (not outside)
def function(variable):
    variable -= variable
    print(variable)
function(7)
# Parameters are variables in a function definition, and arguments are the values put into parameters when functions
# are called


print("24. Returning from Functions")
# int() or str() functions return a value
# Use return statement
def max(x, y):
    if x >= y:
        return x
    else:
        return y
print(max(4, 7))
z = max(8, 9)
print(z)
# Return statement cannot be used outside of a function definition
# Any code after return will never happen
def addNumbers(x, y):
    total = x + y
    return total
    print("This won't happen")
print(addNumbers(10, 20))


print("25. Comments and Doc Strings")
# Comments are creating by using octothorpe (#)
x = 365
y = 7
# this is a comment
print(x % y) # find the remainder
# print(x // y)
# another comment
# Docstrings
# creating by putting multiline string containing an explanation of the function below the function's first line
def shout(word):
    """
    Print a word with an exclamation mark following it
    :param word:
    :return: void
    """
    print(word + "!")
shout("spam")


print("26. Functions as objects")
# Functions are just like any other kind of value
def multiply(x, y):
    return x * y
a = 4
b = 7
operation = multiply
print(operation(a, b))
# We assign the funciton multiply to a variable operation.
# Now operation can also b used to call the function.
# Functions can also e used as arguments of other functions
def add(x, y):
    return x + y
def doTwice(func, x, y):
    return func(func(x, y), func(x, y))
a = 5
b = 10
print(doTwice(add, a, b))


print("27. Modules")
# Code written by other people to fulfill some tasks
# use import statement to import modules
# use import moduleName to import module
# use moduleName.var to access functions
import random
for i in range(5):
    value = random.randint(1, 6)
    print(value)
# Use randint function defined in random module
# Can also use import statement in other format, if we only need certain functions from that module
# Comma separated for multiple imports
from math import pi, sqrt
print(pi)
# Import everything
# from math import *
# This is discouraged, as it confuses variables in our code with variables in external module.
# Import module that isn't available causes ImportError
# Import some module using different name.
from math import sqrt as square_root
print(square_root(100))


print("28. The Standard library and Pip")
# those who we get preinstalled with python is called the standard library
# These are : string, re, datetime, math, random, os, multiprocessing, subprocess, socket, email, json
# doctest, unittest, pdb, argparse and sys.
# Documentation is available at www.python.org
# Third party modules are stored on Python Package Index (PyPI)
# Install them using pip
