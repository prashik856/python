# Hello world program
print("1. INTRODUCTION")
print("Hello World")
# Can also be used to output multiple lines of text
print("Hello world")
print("Spam and Eggs")
print()


# Operations
print("2. OPERATIONS")
print(2+2)
print(5+4-3)
# Addition : +
# Substraction: -
# Multiplication: *
# Division: /
print(2*(3*4))
print(10/2)


# Using a single slash to divide numbers produces a decimal (or float)
# Floats : aren't integers
print("3. FLOATS")
print(3/4)
print(0.42)
# float can also be produced by running any operation on float.
print(8/2)
print(6*5.44)
print(4+10.22)


print("4. EXPONENTIATION")
# Exponentiation: **
print(2**5)
print(2**5**2) # Chain exponentiations
# Can also use floats in exponentiation
print(9**(1/2))


print("5.QUOTIENT AND REMAINDER")
# Floor division : // : Used to determine the quotient of a division
print(20//6) # Outputs 3
# Modulo Operator: % : Used to get remainder
print(20%6)
print(1.25%0.5)


print("6. STRINGS")
# string is created by text in between two single or double quotation marks
print("Python is fun!")
print('Always look on the bright side')
# delimiter " or ' used for a string doesn't affect how it behaves in any way
# Backslash: For special characters.
print('Brian\'s mother: He\'s not an angel. He\'s a very naughty boy!')
# Backslashes can be used to excape tabs, arbitrary Unicode characters, and various other things
# that can't be reliably printed.


print("7. STRING CONCATENATION")
print("Spam" + 'eggs')
print("2" + "2")
# Adding a string to number produces an error.
# Even though they might look similar, they are two different entities.
# Strings can be multiplied.
print("Spam" * 3) # Outputs SpamSpamSpam
print(4 * '2') # Outputs 2222
# Strings can't be multiplied by other strings or floats


print("8. Variables")
user = "James"
x = 7
print(x)
print(x+7)
print(x)
# Can be reassigned as many times as we want.
# No need to include any specific types.
x = 123.232
print(x)
x = "This is a string"
print(x)
# This is not a good practice. To avoid mistakes, try to avoid overwriting the same
# variable with different data types.
# The only characters that are allowed in variable name are letters, numbers and underscores.
# Variable name can't start with a number.
this_is_a_normal_name = 7
#123abc = 7 # Error
# Python is a case sensitive programming language.
# lastname and Lastname is not the same.
# Remove a variable using del
foo = 3
del foo
print(foo)
foo = 2
bar = 3
del bar
bar = 8
print(foo*bar)
# foo and bar are called metasyntactic variables, meaning that they are used as
# placeholder names.


print("9. Taking User Input")
x = input()
print(x)
# Even if the user enters a number, it is processed as string
name = input("Enter your name: ")
print("Hello, " + name)
# Convert string to int
age = int(input())
print(age)
# To convert any number (int) to string, use str()
age = 42
print("His age is " + str(age))
# We can convert to float using float() function
# Multiple inputs
name = input()
age = input()
print(name + " is " + age)


print("10. In place Operators")
x = 2
print(x)
x += 3 # x = x + 3
print(x)
# We can do the same with -, *, / and % as well
# Can also be used on strings
x = "spam"
print(x)
x += "eggs"
print(x)
# In place operators can be used for any numerical operation (+, -, *, /, %, **, //)

