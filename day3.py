# Day 3 — Functions
# Topics:
# 1. Default Arguments
# 2. *args
# 3. **kwargs
# 4. Returning Multiple Values
# 5. Scope — Local vs Global


# ============================================================
# 1. DEFAULT ARGUMENTS
# ============================================================

# A default argument has a value that is used when
# no value is provided while calling the function.

def greet(name, message="Hello"):
    print(message, name)


greet("Aryan")
greet("Aryan", "Good morning")

# If a value is provided, it overrides the default value.


def power(number, exponent=2):
    return number ** exponent


print(power(5))       # 25
print(power(5, 3))    # 125

# Required parameters should come before default parameters.


# ============================================================
# 2. *args
# ============================================================

# *args allows a function to accept any number of
# positional arguments.
#
# The arguments are collected into a tuple.

def show(*args):
    print(args)


show("apple", "banana", "mango")
# ('apple', 'banana', 'mango')


def add(*numbers):
    total = 0

    for number in numbers:
        total += number

    return total


print(add(10, 20))              # 30
print(add(10, 20, 30))          # 60
print(add(10, 20, 30, 40))      # 100


# ============================================================
# 3. **kwargs
# ============================================================

# **kwargs allows a function to accept any number of
# keyword arguments.
#
# The arguments are collected into a dictionary.

def show_details(**kwargs):
    print(kwargs)


show_details(name="Aryan", age=22, course="BTech")
# {'name': 'Aryan', 'age': 22, 'course': 'BTech'}


def display_details(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


display_details(
    name="Aryan",
    age=22,
    course="BTech"
)

# *args       -> positional arguments -> tuple
# **kwargs    -> keyword arguments   -> dictionary


# ============================================================
# 4. RETURNING MULTIPLE VALUES
# ============================================================

# A function can return multiple values.
# Python packs them into a tuple.

def calculate(a, b):
    return a + b, a - b


result = calculate(10, 5)

print(result)
# (15, 5)


# The values can be unpacked into separate variables.

sum_value, difference = calculate(10, 5)

print(sum_value)       # 15
print(difference)      # 5


def get_student():
    name = "Aryan"
    age = 22
    course = "BTech"

    return name, age, course


name, age, course = get_student()

print(name)
print(age)
print(course)


# ============================================================
# 5. SCOPE — LOCAL VS GLOBAL
# ============================================================

# Scope determines where a variable can be accessed.


# LOCAL VARIABLE
# A variable created inside a function is local to that function.

def local_example():
    message = "Hello"
    print(message)


local_example()


# GLOBAL VARIABLE
# A variable created outside a function is global.

name = "Aryan"


def global_example():
    print(name)


global_example()


# A local variable with the same name does not modify
# the global variable.

count = 10


def change_count():
    count = 20
    print(count)


change_count()

print(count)    # 10


# global KEYWORD
# The global keyword allows a function to modify
# a global variable.

count = 10


def update_count():
    global count
    count = 20


update_count()

print(count)    # 20


# ============================================================
# QUICK REVISION
# ============================================================

# Default Arguments
# -> Uses a default value when no value is provided.
#
# *args
# -> Accepts multiple positional arguments.
# -> Stored as a tuple.
#
# **kwargs
# -> Accepts multiple keyword arguments.
# -> Stored as a dictionary.
#
# Returning Multiple Values
# -> Multiple values are packed into a tuple.
# -> They can be unpacked into separate variables.
#
# Local Variable
# -> Created inside a function.
#
# Global Variable
# -> Created outside a function.
#
# global
# -> Allows a function to modify a global variable.