# Python Data Types
# -----------------
# In Python, every value has a data type.
# You can use the built-in type() function to check the data type of value.
# In Python, everything is an object, and all data types are instances of classes — even basic types like int, str, and bool. Here's what that means:
# The type() of that class (like int, str) is type, which is the **metaclass** for all classes in Python.
# All classes themselves are objects of the type class.

# Numeric Types
# -------------
# int: Whole numbers (positive or negative)
age = 21
print(type(age))  # <class 'int'>

# float: Decimal numbers
price = 19.99
print(type(price))  # <class 'float'>

# Complex numbers (less common)
complex_number = 2 + 3j
print(type(complex_number))  # <class 'complex'>

# Text Type
# ---------
# str: Textual data (strings)
name = "Alice"
print(type(name))  # <class 'str'>

# Boolean Type
# ------------
# bool: True or False
is_student = True
print(type(is_student))  # <class 'bool'>

# Sequence Types
# --------------
# list: Ordered, changeable collection
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # <class 'list'>

# tuple: Ordered, unchangeable collection
coordinates = (10.0, 20.0,30.29)
print(type(coordinates))  # <class 'tuple'>

# range: Sequence of numbers (used in loops)
numbers = range(5)
print(type(numbers))  # <class 'range'>

# Mapping Type (dict:dictionary)
# ------------
# dict: Key-value pairs
person = {
    "name": "Alice",
    "age": 30
}
print(type(person))  # <class 'dict'>

# Set Types
# ---------
# set: Unordered collection of unique items
unique_numbers = {1, 2, 3}
print(type(unique_numbers))  # <class 'set'>

# frozenset: Immutable set
frozen = frozenset([1, 2, 3])
print(type(frozen))  # <class 'frozenset'>

# None Type
# ---------
# NoneType: Represents the absence of a value
empty = None
print(type(empty))  # <class 'NoneType'>

# Summary
# -------
# Use type() to check the data type of any value or variable.
# Data types help Python know what kind of operations can be performed.

# Bonus tip: You can also convert types (called casting)
# Example:
number_as_string = "123"
converted = int(number_as_string)
print(type(converted))  # <class 'int'>
