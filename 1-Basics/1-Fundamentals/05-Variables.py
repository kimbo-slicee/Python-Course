"""
This file explains variables and naming conventions in Python,
including case sensitivity.
"""

#----------------------------------
# Additional Info
# Source Code: Original Code You Write it in Computer
# Translation: Converting Code Into Machine Language
# Compilation: Translate Code Before run Time
# Run-Time:Period App Take Tp Executing Commands
# Interpreted: Code Translated On the Fly During Execution
# -------------------------------

# -------------------------------
# VARIABLES IN PYTHON
#--------------------------------
# A variable is used to store data. You can think of it as a container for values.

# Example:
name = "me"            # String variable
age = 25                  # Integer variable
height = 1.70             # Float variable
is_student = True         # Boolean variable

# Python is dynamically typed, so you don’t need to declare the type explicitly.


# -------------------------------
# CASE SENSITIVITY IN PYTHON
# -------------------------------

# Python is **case-sensitive**.
# This means that `Name`, `name`, and `NAME` are three different variables.

name = "Alice"
Name = "Bob"
NAME = "Charlie"

print(name)   # Outputs: Alice
print(Name)   # Outputs: Bob
print(NAME)   # Outputs: Charlie

# So be careful when naming variables—capitalization matters!


# -------------------------------
# NAMING CONVENTIONS IN PYTHON
# -------------------------------

# Python follows certain naming conventions recommended by PEP 8.
# PEP 8 is the style guide for Python code.

# ✅ Valid and recommended naming styles:

# 1. snake_case: for variables and functions
user_name = "Alice"
def get_user_name():
    return user_name

# 2. PascalCase: for classes
class StudentProfile:
    pass

# 3. UPPER_CASE: for constants
PI = 3.14159
MAX_CONNECTIONS = 10

# ❌ Avoid these:
# - camelCase (common in JavaScript, not Python)
# - starting variable names with numbers or special characters
# - using single letters (except in loops or very short-lived variables)

# Bad examples (avoid):
# userName = "Bob"     # camelCase, not recommended
# 2cool = True         # starts with a number, invalid
# $price = 100         # special character, invalid


# -------------------------------
# SPECIAL NAMING RULES
# -------------------------------

# _single_leading_underscore: "private" variable by convention
_internal_value = 42

# __double_leading_underscore: triggers name mangling (used in classes)
class MyClass:
    def __init__(self):
        self.__secret = "hidden"

# __double_underscores__: reserved for special Python methods (also called "dunder" methods)
def __init__(self):
    pass
#----------------------------
# Reserved Keywords in Python
#----------------------------
# use function help
help("keywords") # return a lise of reserved keywords in pyhon you can note declare variable with this names
#----------------------------
# Deleter multiple variables in single line of code
#----------------------------
a,b,c=1,2,3
print(a)
print(b)
print(c)
# -------------------------------
# SUMMARY
# -------------------------------

# ✅ Use meaningful names
# ✅ Use snake_case for variables/functions
# ✅ Use PascalCase for classes
# ✅ Use UPPER_CASE for constants
# ✅ Remember Python is case-sensitive!
# ❌ Avoid using unclear or inconsistent names

