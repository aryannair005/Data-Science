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
9. Inheritance
   - Single level
   - Multilevel
   - Multiple
10. Abstraction
11. Polymorphism
   - Method overriding
   - Duck typing

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

stu = Info()
print(stu.name, stu.branch)


# ==============================
# Constructor (__init__) & Instance Methods
# ==============================

class Student:
    def __init__(self, name, branch):
        self.name = name
        self.branch = branch

    def return_name(self):
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
        self.name = name
        self.branch = branch
        self.PI = 3.14            # instance attribute

    def get_name(self):
        print(f"The name of the student is {self.name}")

c1 = College_Info("aryan", "btech CSE")

print(c1.PI)
print(College_Info.PI)
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
# Class Variable (Object Counter)
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

    def get_balance(self):
        return self.__balance

    def set_balance(self, newBalance):
        self.__balance = newBalance

b = BankAccount("aryan", 10_000)

b.set_balance(20_000)
print(b.get_balance())

# Name mangling (not recommended for regular use)
print(b._BankAccount__balance)


# ==============================
# Inheritance
# ==============================

# Single level inheritance
class Employee:
    start_time = "09:00 am"
    end_time = "05:00 pm"

class Teacher(Employee):
    def __init__(self, subject):
        self.subject = subject


# Multilevel inheritance
class Hod(Teacher):
    def __init__(self, department, subject):
        super().__init__(subject)
        self.department = department


# Multiple inheritance
class CollegeStudent:
    def __init__(self, gpa):
        self.gpa = gpa

class TA(Teacher, CollegeStudent):
    def __init__(self, gpa, subject, name):
        Teacher.__init__(self, subject)
        CollegeStudent.__init__(self, gpa)
        self.name = name


# ==============================
# Abstraction
# ==============================

from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Bow")

class Cat(Animal):
    def sound(self):
        print("Meow")


# ==============================
# Polymorphism
# ==============================

# Method Overriding
class Watch:
    def cost(self):
        print("10000")

class Rolex(Watch):
    def cost(self):
        print("150000")


# Duck Typing
class CollegeTeacher:
    def get_salary(self):
        print("10000")

class CollegeDean:
    def get_salary(self):
        print("14000")

ct = CollegeTeacher()
ct.get_salary()

cd = CollegeDean()
cd.get_salary()
