print("46. Functional Programming")
# Based on functions
# Key part is higher order functions
# Takes functions as arguments
# Pure functions: returns a value that depends only on their arguments
# Pure Functions
def pureFunction(x, y):
    temp = x + 2*y
    return temp / (2*x + y)
#Impure Functions
someList = []
def impure(arg):
    someList.append(arg)
# The function above is not pure because it changed the value of someList
# Pure Functions are
# Easier to reason about and test
# more efficient
# Once the function has been evaluated for an input, the result can be stored and referred
# to the next time the function of that input is needed, reducing the number of times the function is called.
# This is called memoization
# Easier to run in parallel


print("47. Lambdas")
# lambda syntax. They are known as anonymous.
# This is used when passing a simple function as an argument to another function
def myFunction(f, arg):
    return(f(arg))
myFunction(lambda x: 2*x*x, 5)
# lambda functions do thing that only require a single expression
# named function
def polynomial(x):
    return x**2 + 5*x + 4
print(polynomial(-4))
# lambda
print((lambda x: x**2 + 5*x + 4)(-4))
# We created an anonymous function on the fly and called it with an argument
# lambda functions can be assigned to variables and used like normal functions
double = lambda x: x*2
print(double(7))
# It is usually better to define a function with def instead if we assigning a labmda to a variable and then using it
# as a function


print("48. map and filters")
# maps and filter are higher order functions that works on lists (iterables)
# map takes a function and an iterable as arguments, and returns a new iterable with the function applied to each
# argument
def addFive(x):
    return x + 5
nums = [11, 22, 33, 44, 55]
result = list(map(addFive, nums))
print(result)
# Same result using lambda
nums = [11, 22, 33, 44, 55]
result = list(map(lambda x: x+5, nums))
# filter
# The function filter filters an iterable by removing items that don't match a perdicate
# ( a function that returns a Boolean)
nums = [11, 22, 33, 44, 55]
res = list(filter(lambda x: x % 2 == 0, nums))
print(res)


print("49. Generators")
# type of iterable like lists or tuples
# Unlike lists, they don't allow indexing with arbitrary indices, but they
# can still be iterated through with for loops
# They can be created using functions and the yield statement
def countdown():
    i = 5
    while i > 0:
        yield i
        i -= 1
for i in countdown():
    print(i)
# The yield statement is used to define a generator, replacing the return of a function to
# provide a result to its caller without destroying local variables.
# Since yield one item at a time, generators don't have the memory restrictions of lists.
# In fact they can be infinite
def infiniteSevens():
    while True:
        yield 7
for i in infiniteSevens():
    print(i)
# In short, generators allow us to declare a function that behaves like an iterator i.e. it can be used
# in a for loop.
# Finite generators can be converted into lists by passing them as arguments to list function
def numbers(x):
    for i in range(x):
        if i % 2 == 0:
            yield i
print(list(numbers(11)))
# Using generators results in improved performance, which is the result of the lazy (on demand) generation if values,
# which translates to lower memory usage.
# Furthermore, we do not need to wait until all the elements have been generataed before we start to use them.


print("50. Decorators")
# Decorators provide a way to modify functions using other functions
def decor(func):
    def wrap():
        print("======================")
        func()
        print("======================")
    return wrap
@decor
def printText():
    print("Hello World")
decorated = decor(printText)
decorated()
# A single function can have multiple decorators


print("51. Recursion")
# Self reference
# Classic example: Factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)
print(factorial(5))
# Base case acts as the exit condition
# If recursion is infinitie, it will throw RuntimeError
# Indirect recursion.
def isEven(x):
    if x == 0:
        return True
    else:
        return isOdd(x-1)
def isOdd(x):
    return not isEven(x)
print(isOdd(17))
print(isEven(23))


print("52. Sets")
# Sets are data structures similar to lists or dictionaries
# Created using curly braces, or the set function.
# Can use in statement
numSet = {1, 2, 3, 4, 5}
wordSet = set(["spam", "eggs", "sausage"])
print(3 in numSet)
print("spam" not in wordSet)
# To create an empty set, we must use set(), as {} creates an empty dictionary
# Can also use 'len' function
# Sets are unordered (no indexing)
# Cannot contain duplicate elements
# faster to check if element is a part of set
# add method
# remove method
# pop removes arbitrary element
nums = {1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 3, 4}
print(nums)
nums.add(-7)
nums.remove(3)
print(nums)
# Basic uses of sets include membership testing and the elimination of duplicate entries
# union: combines operator |
# intersection: operator & get common item
# difference: operator - get items in first but not in second
# symmetric difference: operator ^ get items in either set but no both
first = {1, 2, 3, 4, 5, 6}
second = {4, 5, 6, 7, 8, 9}
print(first | second)
print(first & second)
print(first - second)
print(second - first)
print(first ^ second)
# data structures
# lists, dictionaries, typles, sets
# When to use dictionary:
# key:value pair
# Fast lookup based on custom key
# Data is being constantly modified
# When to use other types:
# Use lists when we have collection of data that does not need random access.
# Use set if we need uniqueness for elements
# Use tuples when data cannot change
# Use tuples with dictionary as keys, since tuples are immutable.


print("53. Itertools")
# Module itertools
# count function: counts up to infinity
# cycle function: infinitely iterates throguh an interable
# repeat function: repeats an object, either infinitely or a specific number of times
from itertools import count
for i in count(3):
    print(i)
    if i>=11:
        break
# takewhile: takes items from an iterable while a predicate function remains true
# chain: combines several iterables into one long one
# accumulate: returns a running total of values in an iterable
from itertools import accumulate, takewhile
nums = list(accumulate(range(8)))
print(nums)
print(list(takewhile(lambda x: x <= 6, nums)))
# product and permutation functions
from itertools import product, permutations
letters = ("A", "B")
print(list(product(letters, range(2))))
print(list(permutations(letters)))
