# FILE HANDLING PRACTICE

# Create and write to a file
with open("file.txt", "w") as file:
    file.write("Rahul\n")
    file.write("Aryan\n")
    file.write("Rohan\n")


# Read the entire file
with open("file.txt", "r") as file:
    data = file.read()

print("Full file:")
print(data)


# Read one line
with open("file.txt", "r") as file:
    line = file.readline()

print("First line:")
print(line)


# Read all lines as a list
with open("file.txt", "r") as file:
    lines = file.readlines()

print("Lines:")
print(lines)


# Loop through the file
print("Names:")
with open("file.txt", "r") as file:
    for line in file:
        print(line.strip())


# Append new content
with open("file.txt", "a") as file:
    file.write("Ankit\n")


# Check if file exists
import os

if os.path.exists("file.txt"):
    print("File exists")
else:
    print("File does not exist")