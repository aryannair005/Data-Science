"""
Topic: Python Control Flow & Functions (Programming Fundamentals)

Concepts Covered:
1. Conditional Statements (if, elif, else)
2. Nested Conditional Statements
3. Odd / Even Check
4. Match-Case Statement
5. Loops
   - while loop
   - for loop
   - break & continue
6. Range Function
7. String Traversal
8. Counting Vowels
9. Sum of N Natural Numbers
10. Functions
11. Lambda Functions
12. Factorial of a Number

Purpose:
- Learn Python decision making
- Understand looping constructs
- Practice functions
- Build strong Python fundamentals

Language: Python
Author: Aryan Nair
"""

# Conditional Statements
age = 18

if age < 13:
    print("child")
elif age > 13 and age < 18:
    print("next year")
else:
    print("adult")


# Nested Conditional Statements
username = input("enter username: ")
password = input("enter password: ")

if username == "admin" and password == "pass":
    print("logged in")
else:
    if username == "admin":
        print("wrong password")
    else:
        print("wrong username")


# Odd or Even
n = int(input("enter number: "))

if n % 2 == 0:
    print("even")
else:
    print("odd")


# Match Case
color = input("enter color: ")

match color:
    case "green":
        print("go")
    case "red":
        print("stop")
    case "orange":
        print("wait for a while")


# While Loop (Table)
n = int(input("enter number: "))
i = 1

while i <= 10:
    print(i * n)
    i += 1


# Break / Continue
i = 1
while i <= 5:
    if i == 3:
        i += 1
        continue
    print(i)
    i += 1


# For Loop (String Traversal)
Name = "Aryn"

for ch in Name:
    print(ch)

if 'a' in Name:
    print("a is present")
else:
    print("a is not present")


# Range Function
for i in range(5):
    print(i)

for i in range(6, 1, -2):
    print(i)


# Count Vowels
count = 0
word = "artificial intelligence"

for ch in word:
    if ch in 'aeiou':
        count += 1

print(count)


# Sum of N Natural Numbers
n = int(input("enter number: "))
sum = 0

for i in range(1, n + 1):
    sum += i

print(sum)


# Functions
def printHello(a, b):
    print("hello")
    return a + b

print(printHello(3, 4))


# Lambda Function (Average)
a = int(input("enter num 1: "))
b = int(input("enter num 2: "))
c = int(input("enter num 3: "))

average = lambda a, b, c: (a + b + c) / 3
print(average(a, b, c))


# Factorial
n = int(input("enter number: "))

def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

print(factorial(n))
