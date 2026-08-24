# Function Arguments


# 1. Default Arguments
#
# A default argument already has a value.
# If no value is passed, the default is used.

def greet(name="Aryan"):
    print("Hello", name)

greet()          # Hello Aryan
greet("Rahul")   # Hello Rahul


# Multiple default arguments

def student(name, age=22, course="BTech"):
    print(name, age, course)

student("Aryan")              # Aryan 22 BTech
student("Rahul", 25)          # Rahul 25 BTech
student("Sam", 21, "MBA")     # Sam 21 MBA


# Non-default arguments must come before default arguments.

def test(a, b=10):
    pass

# def test(a=10, b):   # Wrong


# Keyword arguments
# We can directly specify which argument we want to change.

student("Aryan", course="MBA")
# Aryan 22 MBA


# 2. *args
#
# *args lets us pass any number of positional arguments.
# Python stores them as a tuple.

def add(*args):
    total = 0

    for num in args:
        total += num

    return total

print(add(10, 20))             # 30
print(add(10, 20, 30))         # 60
print(add(10, 20, 30, 40))     # 100


# Normal argument + *args

def marks(name, *marks):
    print(name)
    print(marks)

marks("Aryan", 80, 90, 85)

# Aryan
# (80, 90, 85)


# 3. **kwargs
#
# **kwargs lets us pass any number of keyword arguments.
# Python stores them as a dictionary.

def info(**kwargs):
    print(kwargs)

info(name="Aryan", age=22, course="BTech")

# {'name': 'Aryan', 'age': 22, 'course': 'BTech'}


# Accessing values

def info(**kwargs):
    print(kwargs["name"])
    print(kwargs["age"])

info(name="Rahul", age=25)

# Rahul
# 25


# *args and **kwargs together

def test(*args, **kwargs):
    print(args)
    print(kwargs)

test(10, 20, name="Aryan", age=22)

# (10, 20)
# {'name': 'Aryan', 'age': 22}


# Quick revision:
#
# Default argument -> used if no value is provided
# *args           -> multiple positional arguments -> tuple
# **kwargs        -> multiple keyword arguments   -> dictionary