"""
Topic: Object Oriented Programming (Python Fundamentals)

This file demonstrates core Object Oriented Programming concepts in Python.

Concepts Covered:
1. Class & Object
2. Constructor (__init__)
3. Instance Methods
4. Class Attributes vs Instance Attributes
5. Class Methods
6. Static Methods
7. Object Counter using Class Variable
8. Encapsulation
   - Private variables
   - Getters & Setters

Purpose:
- Understand OOP concepts
- Learn how classes and objects work
- Practice methods and attributes
- Build strong Python OOP foundation

Language: Python
Author: Aryan Nair
"""

# ==============================
# Class & Object
# ==============================

class Info:
    name = "Aryan"
    branch = "Btech cse"

# Creating object
stu = Info()
print(stu.name, stu.branch)


# ==============================
# Constructor (__init__) & Methods
# ==============================

class Student:
    def __init__(self, name, branch):   # parameterized constructor
        self.name = name
        self.branch = branch

    def return_name(self):              # instance method
        return self.name

s1 = Student("Aryan", "Btech cse")
s2 = Student("Sanjana", "Btech cse")

print(s2.return_name())


# ==============================
# Class Attribute vs Instance Attribute
# ==============================

class College_Info:
    college_name = "IIT Bombay"   # class attribute
    PI = 3.1

    def __init__(self, name, branch):
        self.name = name          # instance attribute
        self.branch = branch
        self.PI = 3.14            # instance attribute (overrides class)

    def get_name(self):
        print(f"The name of the student is {self.name}")

c1 = College_Info("aryan", "btech CSE")

print(c1.PI)             # instance attribute
print(College_Info.PI)   # class attribute
c1.get_name()


# ==============================
# Class Method & Static Method
# ==============================

class Cars:
    seats = 4

    def __init__(self, tyres, lights):
        self.tyres = tyres
        self.lights = lights

    @classmethod
    def get_seat_counts(cls):
        print(f"No. of seats in car are {cls.seats}")

    @staticmethod
    def get_discount(price, discount):
        final_price = (price * discount) / 100
        return price - final_price

c = Cars(5, 20)
print(Cars.get_discount(40_000, 10))


# ==============================
# Class Variable Example (Object Counter)
# ==============================

class Product:
    count = 0

    def __init__(self, name, price):
        self.name = name
        self.price = price
        Product.count += 1

    @staticmethod
    def getDiscount(price, discount):
        return (price * discount) / 100

p1 = Product("pen", 10)
p2 = Product("car", 40_000)

print(Product.count)


# ==============================
# Encapsulation
# ==============================

class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance   # private variable

    # Getter
    def get_balance(self):
        return self.__balance

    # Setter
    def set_balance(self, newBalance):
        self.__balance = newBalance

b = BankAccount("aryan", 10_000)

b.set_balance(20_000)
print(b.get_balance())

# Accessing private variable using name mangling (not recommended)
print(b._BankAccount__balance)
