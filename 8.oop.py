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
# An example magic