# ==========================================
# 1. STRING METHODS
# ==========================================

text = "   hello python world   "


# .strip()
# Removes spaces from the beginning and end

print(text.strip())
# hello python world


# .split()
# Converts a string into a list

sentence = "hello python world"

words = sentence.split()

print(words)
# ['hello', 'python', 'world']

# You can also split using a specific separator
data = "apple,banana,mango"

fruits = data.split(",")

print(fruits)
# ['apple', 'banana', 'mango']


# .join()
# Converts a list into a string

words = ["hello", "python", "world"]

result = " ".join(words)

print(result)
# hello python world

result = "-".join(words)

print(result)
# hello-python-world


# .replace()
# Replaces part of a string

text = "I love Java"

text = text.replace("Java", "Python")

print(text)
# I love Python


# ==========================================
# 2. F-STRINGS
# ==========================================

name = "Aryan"
age = 22

print(f"My name is {name} and I am {age} years old.")

# My name is Aryan and I am 22 years old.


# Expressions can also be used

a = 10
b = 20

print(f"The sum is {a + b}")
# The sum is 30


# ==========================================
# 3. .format()
# ==========================================

name = "Aryan"
age = 22

print("My name is {} and I am {} years old.".format(name, age))

# My name is Aryan and I am 22 years old.


# You can specify positions

print("I am {1} years old and my name is {0}.".format(name, age))


# You can use named values

print(
    "My name is {name} and I am {age} years old.".format(
        name=name,
        age=age
    )
)


# ==========================================
# REAL-WORLD EXAMPLE
# ==========================================

raw_data = "   Aryan,22,Developer   "

# Remove unnecessary spaces
raw_data = raw_data.strip()

# Split into separate values
data = raw_data.split(",")

name = data[0]
age = data[1]
role = data[2]

# Clean output using f-string
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Role: {role}")


# ==========================================
# QUICK SUMMARY
# ==========================================

text = "  hello world  "

text.strip()              # "hello world"
text.split()              # ["hello", "world"]
" ".join(["hello", "world"])  # "hello world"
text.replace("world", "Python") # "  hello Python  "

name = "Aryan"
age = 22

f"{name} is {age}"        # Best/common way
"{} is {}".format(name, age)  # Older alternative