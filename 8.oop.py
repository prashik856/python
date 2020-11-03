print("58. Classes")
# Two paradigms of programming: imperative and functional
# another paradigm is Object-Oriented Programming(OOP)
# Objects are created using classes
# class: object's blueprint
class Cat:
    def __init__(self, color, legs):
        self.color = color
        self.legs = legs
felix = Cat("ginger", 4)
rover = Cat("dog-colored", 4)
stumpy = Cat("brown", 3)
# Two attributes: color and legs
# __init__ method (most imp method)
# Called when a function is created
# All methods must have self as their first parameter.
# within a method definition, self refers to the instance calling method.
# attributes can be accessed using a dot
print(felix.color)
# __init__ method takes two arguments and assigns them to the object's attributes.
# The __init__ method is called the class constructor.
# Classes have methods defined to add functionality to them
# Can be assessed using the same dot expression
class Dog:
    legs = 4
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Woof!")
fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
# Classes can also have class attributes, created by assigning variables within the body of the class
# These can be accessed either from the instance of the class, or the class itself.
# Class attributes are shared by all instances of the class.
# Trying to access an attribute of an instance that isn't defined causes an AttributeError.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
rect = Rectangle(7, 8)
print(rect.color)


print("59. Inheritance")
# Inheritance provides a way to share functionality between classes.
# dogs, cat, rabbit can inherit the superclass Animal.
class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color = color
class Cat(Animal):
    def purr(self):
        print("Purrrr")
class Dog(Animal):
    def bark(self):
        print("Wooof!")
fido = Dog("Fido", "brown")
print(fido.color)
fido.bark()
# A class that inherits from another class is called a subclass
# A class that is inherited from is called a superclass.
# If a class inherits from another with the same attributes or methods, it overrides them
class Wolf:
    def __init__(self, name, color):
        self.name = name
        self.color = color
    def bark(self):
        print("Grrr...")
class Dog(Wolf):
    def bark(self):
        print("Woof!")
husky = Dog("Max", "grey")
husky.bark()
# Wolf is the superclass, and Dog is subclass
# Inheritance can alos be indirect
class A:
    def method(self):
        print("A method")
class B(A):
    def anotherMethod(self):
        print("B method")
class C(B):
    def thirdMethod(self):
        print("C method")
c = C()
c.method()
c.anotherMethod()
c.thirdMethod()
# However, circular inheritance is not possible
# The function super is a useful inheritance-related function that refers to the parent class.
# It can be used to find the method with a certain name in an object's superclass.
class A:
    def spam(self):
        print(1)
class B(A):
    def spam(self):
        print(2)
        super().spam()
B().spam()
# super().spam() calls the spam method of the superclass


print("60. Magic Methods and Operator Overloading")
# Special methods which have double underscores at the beginning and the end of their names
# Also known as dunders
# e.g. __init__
# Common use for them is Operator Overloading
# This means defining operators for custom classes that allow operators which as + and * to be used on them
# An example magic method is __add__ for +
class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
first = Vector2D(5, 7)
second = Vector2D(3, 9)
result = first + second
print(result.x)
print(result.y)
# The __add__ method allows for the definition of a custom behavior for the + operator in our class
# Magic Methods
# __sub__ for -
# __mul__ for *
# __truediv__ for /
# __floordiv__ for //
# __mod__ for %
# __pow__ for **
# __and__ for &
# __xor__ for ^
# __or__ for |
# The expression x+y is translated into x.__add__(y)
class SpecialString:
    def __init__(self, cont):
        self.cont = cont
    def __truediv__(self, other):
        line = "=" * len(other.cont)
        return "\n".join([self.cont, line, other.cont])
spam = SpecialString("spam")
hello = SpecialString("Hello World!")
print(spam/hello)
# Special division operation for our class SpecialString
# Magic methods for comparisons
# __lt__ for <
# __le__ for <=
# __eq__ for ==
# __ne__ for !=
# __gt__ for >
# __ge__ for >=
class SpecialString:
    def __init__(self, cont):
        sefl.cont = cont
    def __gt__(self, other):
        for index in range(len(other.cont) + 1):
            result = other.cont[:index] + ">" + self.cont
            result += ">" + other.cont[index:]
            print(result)
spam = SpecialString("spam")
eggs = SpecialString("eggs")
spam > eggs
# __len__ for len()
# __getitem__ for indexing
# __setitem__ for assigning to indexed values
# __delitem__ for deleting indexed values
# __iter__ for iteration over objects
# __contains__ for in
# __call__ for calling objects
import random
class VagueList:
    def __init__(self, cont):
        self.cont = cont
    def __getitem__(self, item):
        return self.cont[item + random.randint(-1,1)]
    def __len__(self):
        return random.randint(0, len(self.cont)*2)
vagueList = VagueList(["A", "B", "C", "D", "E"])
print(len(vagueList))
print(len(vagueList))
print(vagueList[2])
print(vagueList[2])


print("61. Object Lifecycle")
# Made up of its creation, manipulation, and destruction
# First stage of the life-cycle of an object is the definition of the class to which it belongs
# Destruction of an object occurs when its reference count reaches zero
# Example
a = 42 # Create object <42>
b = a # Increase ref. count of <42>
c = [a] # Increase ref. count of <42>
del a # Decrease ref count of <42>
b = 100 # Decrease ref. count of <42>
c[0] = -1 # Decrease re. count of <42>
# C don't have this kind of automatic memory management


print("62. Data Hiding")
# encapsulation.
# Related concept is data hiding, which states that implementation details of class should be hidden
# We don't have public, private and protected methods
# Weakly private methods and attributes have a single underscore at the beginning.
# It does not stop external code from accessing them.
class Queue:
    def __init__(self, contents):
        self._hiddenlist = list(contents)
    def push(self, value):
        self._hiddenlist.insert(0, value)
    def pop(self):
        return self._hiddenlist.pop(-1)
    def __repr__(self):
        return "Queue({})".format(self._hiddenlist)
queue = Queue([1,2,3])
print(queue)
queue.push(0)
print(queue)
queue.pop()
print(queue)
print(queue._hiddenlist)
# In the code above, the attribute _hiddenlist is marked as private, but it can still be accessed in the outside code.
# The __repr__ magic method is used for string representation of the instance.
# Strongly private methods and attributes have a double underscore.
# These can't be accessed from the outside of the class
# Name mangled methods can still be accessed externally, but by a different name.
# The method __privatemethod of class Spam could be accessed externally with _Spam__privatemethod
class Spam:
    __egg = 7
    def printEgg(self):
        print(self.__egg)
s = Spam()
s.printEgg()
print(s._Spam__egg)
print(s.__egg)
# Basically Python protects those members by internally changing the name to include the class name.


print("63. Class & Static Methods")
# Class methods are different: they are called by a class, which is passed to the cls parameter of the method
# Class methods are marked with a classmethod decorator
# A common use of these are factory methods, which instantiate an instance of a class, using
# different parameters that those usually passed to the class constructor.
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def calculateArea(self):
        return self.width * self.height
    @classmethod
    def newSquare(cls, sideLength):
        return cls(sideLength, sideLength)
square = Rectangle.newSquare(5)
print(square.calculateArea())
# newSquare is a classmethod and is called on the class, rather than on an instance of the class
# It returns a new object of the class cls
# Technically, the parameters self and cls are just conventions; they could be changed to anything else.
# However, they are universally followed, so it is wise to stick to using them.
# Static methods
# Static methods are similar to class methods, except they don't receive any additional arguments.
# They are identical to normal functions that belong to a class.
# They are marked with the staticmethod decorator
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    @staticmethod
    def validatTopping(topping):
        if topping == "pineapple":
            raise ValueError("No pipeapples!")
        else:
            return True
ingredients = ["cheese", "onions", "spam"]
if all(Pizza.validatTopping(i) for i in ingredients)
    pizza = Pizza(ingredients)
# Static methods behave like plain functions, except for the fact that we can call them for an instance of the class.


print("64. Properties")
# Properties provide a way of customizing access to instance attributes
# They are created by putting the property decorator above a method, which means wehn the instance
# attribute with the same name as the method is accessed, the method will be called instead.
# One common-use of property is to make an attribute read-only
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
    @property
    def pineappleAllowed(self):
        return False
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineappleAllowed)
pizza.pineappleAllowed = True
# Properties by using setter/getter functions
# setter sets the corresponding property's value
# getter gets the value
# For setter, we need to use a decorator of the same name as the property, followed by a dot and the setter keyword
# Same for getter
class Pizza:
    def __init__(self, toppings):
        self.toppings = toppings
        self._pineappleAllowed = False
    @property
    def pineappleAllowed(self):
        return self._pineappleAllowed
    @pineappleAllowed.setter
    def pipeappleAllowed(self, value):
        if value:
            password = input("Enter the password: ")
            if password == "Swordfish!":
                self._pineappleAllowed = value
            else:
                raise ValueError("Alert! Introder!")
pizza = Pizza(["cheese", "tomato"])
print(pizza.pineappleAllowed)
pizza.pineappleAllowed = True # Here, the code will ask for password
print(pizza.pineappleAllowed)
