print("29. Exceptions")
# Happens when something goes wrong
num1 = 7
num2 = 0
print(num1/num2)
# ZeroDivisionError: division by zero
# Different exceptions
# ImportError
# IndexError
# NameError
# SyntaxError
# TypeError: a function is called on a value of inappropriate type
# ValueError: a function ia called on a value of the called type, but with an inappropriate value.
# ZeroDivisionError
# OSError
# Third parties define their own exceptions


print("30. Exception Hanlding")
# try and except statements
# try block contains code that might throw exception.
# If exception occurs, the code in try block stops executing, and code in except block runs.
# If no errors occurs, code in try block runs
try:
    num1 = 7
    num2 = 0
    print(num1 / num2)
    print("Done calculation")
except ZeroDivisionError:
    print("An error occured")
    print("Due to zero division error")
# except statement defines the type of exception which will occur
# try can have multiple different except statements
# except statement can have multiple exceptions as arguments
try:
    variable = 10
    print(variable + "Hello")
    print(variable / 2)
except ZeroDivisionError:
    print("Divided by zero")
except(ValueError, TypeError):
    print("Error occured")
# except without any exception catches all exceptions
try:
    word = "spam"
    print(word / 0)
except:
    print("An Error occured")
# Exception handling is very useful when dealing with user input.


print("31. finally")
# finally statement: run some code no matters what
try:
    print("Hello")
    print(1/0)
except ZeroDivisionError:
    print("Divided by zero")
finally:
    print("this code will run no matter what")
# Code in finally statement even runs if uncaught exception occurs
try:
    print(1)
    print(1/0)
except ZeroDivisionError:
    print(unknown_var)
finally:
    print("This is executed last")


print("32. Raising Exceptions")
# using raise statement
print(1)
raise ValueError
print(2)
# Need to specify type of error
# Can provide argument message
name = "123"
raise NameError("Invalid name!")
# In except blocks, the raise statements can be used without arguments to re-raise whatever exception occured
try:
    num = 5/0
except:
    print("An error occured")
    raise


print("33. Assertions")
# Sanity Check
# An expression is tested, if result comes up false, an exception is raised
# Using assert statement
print(1)
assert 2 + 2 == 4
print(2)
assert 1 + 1 == 3
print(3)
# We should put assertions at the start of a function to check for valid input, and after
# a function call to check for valid output.
# Assert can take a second argument that is passed to AssertionError if raised
temp = -10
assert (temp >= 0), "Colder than absolute zero"
# We can also handle assertion error like any other error
