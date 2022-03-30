# Modules should have short, all-lowercases names
# class names in CapWords
print("72. More on Function Arguments")
# Function with varying number of arguments
# Using *args as a function parameter enables us to pass an arbitrary number of arguments
# to that function
# The arguments are then accessible as the tuple args in the body of the function
def function(namedArg, *args):
    print(namedArg)
    print(args)
function(1,2,3,4,5,6)
# The parameter *args must come after the named parameters to a function.
# The number args is just a convention. We can choose to use another.
# Named parameters to a function can be made optional by giving them a default value.
# These must come after named parameters without a default value.
def function(x, y, food="spam"):
    print(food)
function(1, 2)
function(1, 2, "egg")
# **kwargs (standing for keyword arguments
# Allows us to handle named arguments that we have not defined in advanced.
# The keyword arguments return a dictionary in which the keys are the argument names, and the
# values are the argument values
def myFunc(x, y=7, *args, **kwargs):
    print(kwargs)
myFunc(2,3,4,5,6,a=7,b=8)
# The arguments returned by **kwargs are not included in *args


print("73. Tuple Unpacking")
# Tuple unpacking allows us to assign each item in an iterable to a variable
numbers = (1,2,3)
a, b, c = numbers
print(a)
print(b)
print(c)
# This can also be used to swap variables by doing a, b = b, a
# since b, a on the right side forms the tuple (b,a), which is then unpacked.
# A variable that is prefaced with an asterisk(*) takes all values from the iterable that are left
# over from the other variables
a, b, *c, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)
print(b)
print(c)
print(d)


print("74. Ternary Operator")
# often useful when assigning variables.
a = 7
b = 1 if a >= 5 else 42
print(b)
status = 1
msg = "Logout" if status == 1 else "Login"
# The ernary operator is so called because, unlike most operators, it takes three arguments


print("75. More on else statements")
# else statement can also follow a for or while loop.
# With a for or while loop, the code within is called if the loop finished normally (when a break statement
# does not cause an exit from the loop)
for i in range(10):
    if i == 99:
        break
else:
    print("Unbroken!")
for i in range(10):
    if i == 5:
        break
else:
    print("Unbroken 2!")
# Unbroken 2! is not printed.
# The first for loop executes normally, thus Unbroken! is printed.
# Else statement can also be used with try/except statements
# The code within will only execute if no error occurs in the try statement
try:
    print(1)
except ZeroDivisionError:
    print(2)
else:
    print(3)
try:
    print(1/0)
except ZeroDivisionError:
    print(4)
else:
    print(5)


print("76. __main__")
# Make a file that can be both imported as a module and run as a script
# To do this, we write if __name__ == "__main__"
# This ensures that it won't be run if the file is imported
def function():
    print("This is a module function")
if __name__ == "__main__":
    print("This is a script")
# If the python interpreter is running that module (the source file) as the main program,
# it sets the special __name__ variable to have a value "__main__".
# If this file is being imported from another module, __name__ will be set to the module's name.
# If we save the code from our previous example as a file called exampleimport.py, we can import
# it to another script as a module, using the name exampleimport
import exampleimport
exampleimport.function()
# Basically we have created a custom module named exampleimport, and used it here.

print("77. Major 3rd party libraries")
# Django/ CherryPy and Flash (Famous Python web development frameworks)
# For scraping data from websites, BeautifulSoup is very useful.
# matplotlib: create graphs
# numpy
# Scipy: extensions of numpy
# Panda3D and pygame for game development


print("78. Packaging")
# Packaging: Putting modules to standard format
# This involves use of modules setuptools and distutils
# Need to organize existing files correctly.
# __init__.py is required. It can be empty.
# setup.py is also required.
# the directory structure required
'''
SoloLearn/
    LICENSE.txt
    README.txt
    setup.py
    sololearn/
        __init__.py
        sololearn.py
        sololearn2.py
'''
# Checkout example setup.py file
# setup.py contains information necessary to assemble the package so it can be uploaded to PyPI
# and installed with pip.
# To build a source distribution, use the command line to navigate to the directory
# containing setup.py and run:
# python setup.py sdist
# python setup.py bdist : for windows
# python setup.py bdist_wininst : to build binary distribution
# python setup.py register followed by python setup.py sdist upload : to register and upload the package
# python setup.py install: install the package.


print("79. Packaging for Users")
# For Windows or Mac.
# For windows: py2exe can be used to package a python script, along with libraries it requires, into a single
# executable file
# PyInstaller and cx_Freeze serve the same purpose.
# For Mac: py2app, PyInstaller or cx_Freeze