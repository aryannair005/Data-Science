"""
Topic: File Handling, Exception Handling & Advanced Python (Programming Fundamentals)

This file demonstrates file operations, exception handling, list comprehensions,
and JSON data handling in Python.

Concepts Covered:
1. File Handling (I/O)
   - Read
   - Readline
   - Write
   - with keyword
   - Delete file
2. Word Search Problem
3. Exception Handling
   - try, except, else, finally
4. List Comprehensions
5. JSON Data Handling
   - JSON strings
   - JSON files

Purpose:
- Learn file operations in Python
- Handle runtime errors safely
- Practice concise syntax using list comprehensions
- Work with JSON data for real-world applications

Language: Python
Author: Aryan Nair
"""

# ==============================
# File Handling (I/O)
# ==============================

# Open a file in read mode
f = open("sample.txt", "r")

# Read entire file
data = f.read()
print(data)

# Read line by line
data1 = f.readline()
print(data1)

# Close the file
f.close()


# Write to a file (overwrite mode)
f = open("sample.txt", "w")
f.write("hello")
f.close()


# Using with keyword (auto closes file)
with open("sample.txt", "r") as f:
    print(f.read())


# Delete a file
import os
os.remove("sample2.txt")


# ==============================
# Word Search Problem
# ==============================

data = True
line = 1

with open("sample.txt", "r") as f:
    while data:
        data = f.readline()
        if "good" in data:
            print(line)
        else:
            line += 1


# ==============================
# Exception Handling
# ==============================

try:
    x = int(input("Enter number: "))
    ans = 10 / x
except ZeroDivisionError:
    print("division by 0 is not allowed")
except ValueError:
    print("Invalid input")
else:
    print(f"ans is {ans}")
finally:
    print("Program runned")


# ==============================
# List Comprehensions
# ==============================

# Square of odd numbers
sq = [i * i for i in range(6) if i % 2 != 0]
print(sq)

# Replace negative numbers with 0
lst = [-2, -4, 3, 5, 2, -1]
lst = [0 if val < 0 else val for val in lst]
print(lst)

# Convert words to upper and lower case
words = ["aryan", "aditya", "dheeraj"]
words = [word.upper() for word in words]
words = [word.lower() for word in words]
print(words)


# ==============================
# JSON Data Handling
# ==============================

import json

# JSON string
json_str = '{"name":"Aryan","branch":"btech cse","student":true}'

# Convert JSON string to Python object
python_obj = json.loads(json_str)

# Python dictionary
python_object = {
    "name": "aryan",
    "student": True
}

# Convert Python object to JSON string
json_obj = json.dumps(python_object)
print(json_obj)
print(type(json_obj))


# ==============================
# JSON with Files
# ==============================

data = {
    "name": "aryan",
    "isStudent": True
}

# Read JSON file and convert to Python object
with open("data.json", "r") as f:
    python_obj = json.load(f)
    print(python_obj)

# Write Python object to JSON file
with open("data.json", "w") as f:
    json.dump(data, f)
