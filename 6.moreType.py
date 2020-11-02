print("38. None")
# None object is used to represent the absence of value
# Similar to null
# False when converted to boolean
None == None
None
print(None)
# None is returned by any function that doesn't return anything
def someFunction():
    print("Hi")
var = someFunction()
print(var)


print("39. Dictionaries")
# Datastructures used to map arbitrary keys to values
# Lists are dictionaries with integer keys
ages = {"Dave": 24, "Mary": 42, "John": 58}
print(ages["Dave"])
print(ages["Mary"])
# Trying to index a key that isn't part of dictionary returns a KeyError
primary = {
    "red": [255, 0, 0],
    "green": [0, 255, 0],
    "blue": [0, 0, 255]
}
print(primary["red"])
print(primary["yellow"])
# Dictionaries can store any type of data as values
# Only immutable objects can be used as keys to dictionaries.
# Immutable objects are those that cannot be changed
# Mutalbe objects example: lists, Dictionaries.
# Trying to use mutalbe object as a dictionary causes a TypeError
badDict = {
    [1, 2, 3]: "one two three"
}


print("40. Dictionary functions")
# dict keys can be assigned to different values
squares = {1: 1, 2: 4, 3: "error", 4: 16}
squares[8] = 64
squares[3] = 9
print(squares)
# To determine whether a key is in a dictionary or not, we can use in and not in.
nums = {
    1: "one",
    2: "two",
    3: "three"
}
print(1 in nums)
print("three" in nums)
print(4 not in nums)
# get method. dict.get(key)
# Same thing as indexing, but if key is not found, None is returned
pairs = {
    1: "apple",
    "orange": [1, 2, 3],
    True: False,
    None: "True"
}
print(pairs.get("orange"))
print(pairs.get(7))
print(pairs.get(12345, "not in dictionary"))


print("41. Tuples")
# Tuples are very similar to lists, except they are immutable
# Created using parentheses
words = ("spam", "eggs", "sausages")
print(words[0])
# Trying to reassign a value in a tuple causes TypeError
words[1] = "cheese"
# tuples can also be created without parentheses, by jus tseparating the values with commas
myTuple = "one", "two", "three"
print(myTuple[0])
# Empth tuple
empty = ()
# Tuples are faster than lists, but they cannot be changed


print("42. List Slices")
# Advanced way of retrieving values
# It will not include the second value
# involves indexing a list with two colon-separated integers.
squares = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(squares[2:6])
print(squares[3:8])
print(squares[0:8])
# If first number is omitted, it is considered as start and vice versa
print(squares[:7])
print(squares[7:])
# Slicing also works on tuples
# Slicing can also have third number which represents step
print(squares[::2])
print(squares[2:8:3])
# Negative values can be used in list slicing and normal list indexing.
# When negative values are used for the first and second values in a slice, they count from the end of the list
print(squares[1:-1])
# Prints 1 ... 64
# If negative value is used for the step, the slice is done backwards
# using [::-1] as a slice is a common and idiomatic way to reverse a list.


print("43. List Comprehensions")
# Useful way of quickly creating lists whose contents obey simple rules
# a list comprehension
cubes = [i**3 for i in range(5)]
# if statement
evens = [i**2 for i in range(10) if i**2 % 2 == 0]
# Trying to create a list in a very extensive range will result in a MemoryError
even = [2*i for i in range(10**100)]
# This issue is resolved by generators


print("44. String Formatting")
# Strings format method to substitute a number of arguments in the string
# string formatting
nums = [4, 5, 6]
msg = "Numbers: {0} {1} {2}".format(nums[0], nums[1], nums2)
print(msg)
# Each argument is placed in the corresponding position
# Can also be done with named arguments
a = "{x}, {y}".format(x=5, y=12)
print(a)


print("45. Useful Functions")
# String functions
# join() - joins a list of strings with another string as a separator
# replace() - replace one substring with another
# startwith() and endswith() - determine if there is substring at start and end of the string
# lower(), and upper()
# split() is apposite of join
print(",".join(["spam", "eggs", "ham"]))
# prints "spam, eggs, ham
print("Hello ME".replace("ME", "world"))
print("This is a sentence.".startswith("This"))
print("This is a sentence.".endswith("sentence."))
print("This is a sentence.".upper())
print("ALL IN CAPS SENTENCE".lower())
print("spam, eggs, ham".split(", "))
# Numeric Functions
# max, min
# To find the distance of a number from zero, abs
# round a number: round
# total of list: sum
print(min(1,2,3,4,5,6,7))
print(max[1,2,3,4,5,6,7])
print(abs(-99))
print(abs(42))
print(sum([1,2,3,4,5,6,7,8]))
# List Functions
# all or any takes a list as an argument and return True if all or any (respectively) of their arguments
# Evaluates to True (or False)
# enumarate() can also be used for iteration
nums = [55, 44, 33, 22, 11]
if all([i>5 for i in nums]):
    print("All larger than 5")
if any([i % 2 == 0 for i in nums]):
    print("At least one is even")
for v in enumerate(nums):
    print(v)
