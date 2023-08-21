# Explanation of Python Syntax, Operators, and Strings

# Syntax:
# Python code is written using a specific syntax that follows indentation.
# Indentation is crucial for defining code blocks like loops and functions.

# Operators:
# Operators perform various operations on variables and values.
# Common operators include arithmetic, assignment, comparison, logical, etc.

# Strings:
# Strings are sequences of characters, enclosed in single (' ') or double (" ") quotes.
# They can be manipulated using various string methods.

# ---------------------
# Python Operators:

# Arithmetic Operators
num1 = 10
num2 = 5
addition = num1 + num2  # Addition operator
subtraction = num1 - num2  # Subtraction operator
multiplication = num1 * num2  # Multiplication operator
division = num1 / num2  # Division operator
modulus = num1 % num2  # Modulus operator (remainder)

# Assignment Operators
x = 10  # Assigning a value
x += 5  # Equivalent to x = x + 5
x -= 3  # Equivalent to x = x - 3
x *= 2  # Equivalent to x = x * 2
x /= 4  # Equivalent to x = x / 4

# Comparison Operators
is_equal = num1 == num2  # Equal to
is_not_equal = num1 != num2  # Not equal to
is_greater = num1 > num2  # Greater than
is_less = num1 < num2  # Less than
is_greater_equal = num1 >= num2  # Greater than or equal to
is_less_equal = num1 <= num2  # Less than or equal to

# Logical Operators
and_result = True and False  # Logical AND
or_result = True or False  # Logical OR
not_result = not True  # Logical NOT

# String Basics:
single_quoted = 'Hello, single quotes!'
double_quoted = "Hello, double quotes!"
concatenation = single_quoted + " " + double_quoted  # Concatenating strings

# String Methods:
message = "   Hello, Python!   "
length = len(message)  # Length of the string
uppercase = message.upper()  # Convert to uppercase
lowercase = message.lower()  # Convert to lowercase
stripped = message.strip()  # Remove leading and trailing spaces

# Output explanations:
print("Arithmetic Operators:")
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)
print("Modulus:", modulus)

print("\nAssignment Operators:")
print("x after operations:", x)

print("\nComparison Operators:")
print("Is equal:", is_equal)
print("Is not equal:", is_not_equal)
print("Is greater:", is_greater)
print("Is less:", is_less)
print("Is greater or equal:", is_greater_equal)
print("Is less or equal:", is_less_equal)

print("\nLogical Operators:")
print("AND Result:", and_result)
print("OR Result:", or_result)
print("NOT Result:", not_result)

print("\nString Basics:")
print("Single Quoted String:", single_quoted)
print("Double Quoted String:", double_quoted)
print("Concatenated String:", concatenation)

print("\nString Methods:")
print("Original Length:", length)
print("Uppercase:", uppercase)
print("Lowercase:", lowercase)
print("Stripped:", stripped)
