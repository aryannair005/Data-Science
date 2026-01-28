"""
Topic: Python Basics (Programming Fundamentals)

This file demonstrates core Python concepts using simple examples.

Concepts Covered:
1. Print Function
2. Variables
3. Data Types
4. Operators
   - Arithmetic
   - Relational / Comparison
   - Assignment
   - Logical
5. Operator Precedence
6. Type Casting
7. User Input
8. Simple Problem: Average of Two Numbers

Purpose:
- Learn Python syntax
- Understand basic operations
- Practice input/output
- Build strong fundamentals before DSA

Language: Python
Author: Aryan Nair
"""

# Print function
print("Hello World \nhi","hi")

# Variables
Pi=3.14
name="Aryan"
print(name)

# Data Types
isPrime=True
print(type(isPrime))

# Operators
a=10
b=2

# Arithmetic
print("a+b",a+b)
print("a-b",a-b)
print("a*b",a*b)
print("a/b",a/b)
print("a%b",a%b)
print("a to the power b",a**b)

# Relational / Comparison 
print(a<b)
print(a>b)
print(a>=b)
print(a<=b)
print(a!=b)

# Assignment
a=b
a+=5
a-=5
a*=10
a/=2
print(a)

# Logical
var=True
print(not var)
print((a>b) and (a<b))
print((a>b) or (a<b))

# Operator precedence
# ()   >   **   >   *,/,% > +,-   > ==,!=,>,>=,<,<=    >    not   > and  > or

# Type Casting
a=int(10*2.1)
print(type(a))

# Input
a=input("Enter value")
print(a)

# Average of two numbers
num1=int(input("Enter a"))
num2=int(input("Enter b"))

print((num1+num2)/2)
