# Returning Multiple Values and Scope


# 1. Returning Multiple Values
#
# A function can return more than one value.
# Python packs the returned values into a tuple.

def calculate(a, b):
    return a + b, a - b

result = calculate(10, 5)

print(result)
# (15, 5)


# We can also unpack the returned tuple directly.

def calculate(a, b):
    return a + b, a - b

addition, subtraction = calculate(10, 5)

print(addition)       # 15
print(subtraction)    # 5


# A function can return any number of values.

def get_info():
    return "Aryan", 22, "BTech"

name, age, course = get_info()

print(name)
print(age)
print(course)


# The number of variables should normally match
# the number of returned values.

a, b = (10, 20)       # Correct

# a, b = (10, 20, 30) # Error


# 2. Scope
#
# Scope means where a variable can be accessed.
#
# Local  -> inside a function
# Global -> outside a function


# Local variable

def greet():
    name = "Aryan"
    print(name)

greet()

# name cannot normally be accessed outside greet()
# because it is a local variable.


# Global variable

name = "Aryan"

def greet():
    print(name)

greet()

# A function can read a global variable.


# Local and global variables can have the same name.

x = 10

def test():
    x = 20
    print(x)

test()
print(x)

# Output:
# 20
# 10
#
# x = 20 is local to test()
# x = 10 is the global variable.
# They are separate variables.


# Changing a global variable inside a function
#
# Use the 'global' keyword when you want to modify
# the global variable.

count = 0

def increase():
    global count
    count += 1

increase()

print(count)
# 1


# Quick revision:
#
# Multiple return values -> returned as a tuple
#
# Example:
# return a, b
# -> (a, b)
#
# Scope:
# Local  -> variable inside a function
# Global -> variable outside a function
#
# To modify a global variable inside a function:
# use the global keyword.