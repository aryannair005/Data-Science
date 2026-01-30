"""
Topic: Python Strings & Data Structures (Programming Fundamentals)

This file demonstrates string operations and core Python data structures.

Concepts Covered:
1. Strings
   - Concatenation
   - Length
   - Indexing
   - Slicing
   - Formatting
2. Lists
   - Mutability
   - List methods
   - Looping
3. Tuples
   - Immutability
   - Tuple methods
4. Dictionary
   - Key-value pairs
   - Dictionary methods
5. Sets
   - Unique elements
   - Set methods
6. Small Problem using List, Set & Dictionary

Purpose:
- Understand strings and collections
- Practice built-in methods
- Learn real-world data handling
- Strengthen Python fundamentals

Language: Python
Author: Aryan Nair
"""

# Strings
word1 = "My name is "
word2 = "Aryan"

# Concatenation
print(word1 + word2)

# Length
print(len(word1) + len(word2))

# Index access
print(word1[4])

# Slicing
print(word1[0:5])
print(word1[:5])
print(word1[5:])

# Reverse indexing
print(word1[-2])


# String Formatting
a = 10
b = 5

# Normal formatting
print("Sum of {} and {} is {}".format(a, b, a + b))

# Index based formatting
print("Sum of {1} and {0} is {2}".format(a, b, a + b))

# Value based formatting
print("{a} and {b}".format(a=10, b=5))

# f-strings
print(f"value of {a} and {b} is {a + b}")


# List (mutable sequence)
marks = [100, 30, 68, 49, 48]

# Modify list element
marks[0] = 89

# List methods
marks.append(60)          # add element at end
marks.insert(0, 10)       # add element at index
marks.sort()              # sort in increasing order
marks.sort(reverse=True)  # sort in decreasing order
marks.reverse()           # reverse list

print(marks)

# Loop on list
i = 0
for mark in marks:
    if mark == 49:
        print(i)
        break
    i += 1


# Tuples (immutable sequence)
tup = (1, 3, 4, 5, 6, 3, 3)
tup2 = (1,)   # single element tuple

sum = 0
for t in tup:
    sum += t

# Tuple methods
print(tup.index(3))   # first occurrence index
print(tup.count(3))   # total occurrences


# Dictionary (key : value pairs)
info = {
    "name": "Aryan",
    "age": 21,
    "marks": 55
}

# Update value
info["name"] = "sanjana"
print(info["name"])

# Dictionary methods
print(info.keys())      # all keys
print(info.values())    # all values
print(info.items())     # key-value pairs
print(info.get("name")) # value using key

# Add new item
info.update({"mood": "happy"})

# Difference between get() and direct access
print(info.get("namee"))   # returns None
# print(info["namee"])     # gives error

print(info)


# Sets (unique elements)
s = {1, 3, 3, 4, 5}
print(s)

# Empty set vs empty dictionary
empty_set = {}
print(type(empty_set))

# Set methods
s.add(5)      # add element
s.remove(4)   # remove element
s.pop()       # remove random element
s.clear()     # remove all elements


# Set operations
s1 = {1, 2, 3, 4}
s2 = {2, 3}

print(s2.union(s1))
print(s2.intersection(s1))


# Small problem using list + dictionary + set
data = [
    ("aryan", "coding"),
    ("talim", "system design"),
    ("sanjana", "hindi"),
    ("aryan", "hindi")
]

dict = {}

for name, course in data:
    if dict.get(name) is None:
        dict.update({name: set()})
        dict[name].add(course)
    else:
        dict[name].add(course)

print(dict)
