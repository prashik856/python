print("11. Booleans")
# Boolean type: True or False
my_boolean = True
print(my_boolean)
print(2 == 3)
print("hello" == "hello")
# = is assignment, whereas == is comparison
# != : Not equal sign
print(1 != 1)
print("eleven" != "seven")
print(1 != 10)
# Comparison operators are also called Relational Operators
# > : greater than
# < : less than
print(7 > 5)
print(10 < 10)
# Integers or floats can also be used
# >= : greater than or equal to
# <= : smaller than or equal to
print(7 <= 8)
print(9 >= 9.0)
# > and < operators can also be used to compare strings lexicographically
# The alphabetical order of words is based on the alphabetical order of their components letters
print("Annie" > "Andy")


print("12. If statements")
# if expression:
#   statement
# Python uses identation
if 10 > 5:
    print("10 is greater than 5")
print("Program ended")
# if can be nested
num = 12
if num > 5:
    print("Bigger than 5")
    if num <= 47:
        print("Between 5 and 47")
# Identation is used to define level of nesting


print("13. Else statement")
x = 4
if x == 5:
    print("Yes")
else:
    print("No")
# Every if statement can have only one else statement
num = 3
if num == 1:
    print("One")
else:
    if num == 2:
        print("Two")
    else:
        if num == 3:
            print("Three")
        else:
            print("Something else")
# Identation determines which if/else statements the code block belong to
# Better to use elif statements rather than multiple if and else statements
num = 3
if num == 1:
    print("One")
elif num == 2:
    print("Two")
elif num == 3:
    print("Three")
else:
    print("Something else")
# A series of if elif statements can have a final else block.


print("14. Boolean Logic")
# and, or , and not.
# Boolean and (True if all are true)
print( 1 == 1 and 2 == 2)
print( 1 == 1 and 2 == 3)
print( 1 != 1 and 2 == 2)
print( 2 < 1 and 3 > 6)
# Boolean or (True if any one is true)
print( 1 == 1 or 2 == 2)
print( 1 == 1 or 2 == 3)
print( 1 != 1 or 2 == 2)
print( 2 < 1 or 3 > 6)
# Boolean not
# Inverts (True to False and False to True)
print(not 1 == 1)
print(not 1 > 7)


print("15. Multiple Operators and Conditions")
# Operator Precedence.
# == has higher precedence than or
print( False == False or True)
print( False == (False or True))
print( (False == False) or True)
# Python follows BODMAS
# Chaining Multiple Conditions
grade = 88
if ( grade >= 70 and grade <= 100):
    print("Passed!")
# Can use multiple and, or, not operators


print("16. Lists")
# Used to store items
# Initialization
words = ["Hello", "world", "!"]
print(words[0])
print(words[1])
print(words[2])
# Create empty list
empty_list = []
print(empty_list)
# List items can have comma at the end
# List can have items of different types
number = 3
things = ["string", 0, [1, 2, number], 4.56]
print(things[1])
print(things[2])
print(things[2][2])
# Initialized 2D Lists
m = [
    [1, 2, 3],
    [4, 5, 6]
]
print(m[1][2])
# String can be indexed like lists
string = "Hello world!"
print(string[6])
# Space (" ") is also a symbol and has an index


print("17. List Operators")
# Reassigning
nums = [7, 7, 7, 7, 7, 7]
nums[2] = 5
print(nums)
# Adding and multiplying lists (same way as strings)
nums = [1, 2, 3]
print(nums + [4, 5, 6])
print(nums * 3)
# Checking if item is in a list (use 'in')
words = ["spam", "egg", "spam", "sausage"]
print("spam" in words)
print("egg" in words)
print("tomato" in words)
# in operator is also used to determine whether or not a string is a substring of another string.
# If an item is not in a list, use 'not'
nums = [1, 2, 3]
print(not 4 in nums)
print(4 not in nums)
print(not 3 in nums)
print(3 not in nums)


print("18. List Functions")
# append method
nums = [1, 2, 3, 4]
print(nums)
# dot before append is there because it is a method of the list class.
# To get the length of list
nums = [1, 3, 5, 7, 9]
print(len(nums))
# len is a function, not a method.
# insert method: similar to append, except it allows us to insert a new item in any position
words = ["Python", "fun"]
index = 1
words.insert(index, "is")
print(words)
# index method: Finds the first occurence of a list item and returns its index
# if item isn't in the list, it raises a ValueError
letters = ["p", "q", "r", "s", "p"]
print(letters.index("r"))
print(letters.index("p"))
print(letters.index("z"))
# max function: max(list): Returns max value
# min function: min(list): Returns min value
# count method: list.count(item): Returns a count of how many times an item occurs in a list
# remove method: list.remove(item): Removes an object from a list
# reverse method: list.reverse(): Reverses items in a list


print("19. While Loops")
i = 1
while i <= 5:
    print(i)
    i = i + 1
print("Finished")
# The code in the body of a while loop is executed repeatedly. This is called iteration
x = 1
while x < 10:
    if x % 2 == 0:
        print(str(x) + " is even")
    else:
        print(str(x) + " is odd")
    x += 1
# str(x) is used to convert the number x to a string. (We used concatenation here)
# break
i = 0
while True:
    print(i)
    i = i + 1
    if i >= 5:
        print("Breaking")
        break
print("Finished")
# Cannot use break outside of a loop
# continue: jumps back to the top of the loop: stops the current iteration and continues with the next one
i = 1
while i <= 5:
    print(i)
    i += 1
    if i == 3:
        print("Skipping 3")
        continue


print("20. For Loops")
words = ["hello", "world", "spam", "eggs"]
for word in words:
    print(word + "!")
# for loop can be used to iterate over strings
string = "testing for loops"
count = 0
for x in string:
    if x == "t":
        count += 1
print(count)
# break and continue statements can be used inside for loops
# for loop when number of iterations is fixed.
# while loop when number of iterations is not known.


print("21. Range")
# range() function: returns a sequence of numbers
# by default, it starts from 0, increments by 1 and stops before the specified number.
numbers = list(range(10))
print(numbers)
# If we want output in list, we need to convert it to list.
# If range is called with two arguments, it produces values from first to second.
numbers = list(range(3, 8))
print(numbers)
print(range(20) == range(0, 20))
# range(3,8) will not include 8
# Third argument determines the interval of the sequence produced. Also called the step.
numbers = list(range(5, 20, 2))
print(numbers)
# List of decreasing numbers can be created by giving step as negative
numbers = list(range(20, 5, -2))
print(numbers)
# for loops with range
for i in range(6):
    print("Hello!")
