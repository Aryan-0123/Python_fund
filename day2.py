person = {
    "name": "Aryan",
    "age": 22,
    "city": "Delhi"
}
print(person.get("name"))          # Aryan
print(person.get("salary"))        # None
print(person.get("salary", 0))     # 0 (default value)


for key, value in person.items():
    print(key, value)

print(person.keys())

for key in person.keys():
    print(key)

for key in person:
    print(key)


# 4. Nested dictionaries
students = {
    "student1": {
        "name": "Aryan",
        "age": 22,
        "marks": 85
    },
    "student2": {
        "name": "Rahul",
        "age": 21,
        "marks": 91
    }
}

# Access nested values
print(students["student1"]["name"])    # Aryan
print(students["student2"]["age"])   # 21


# Loop through nested dictionary
for student_id, student in students.items():
    print(student_id)
    print(student["name"])
    print(student["marks"])


# .get() with nested dictionary
print(students["student1"].get("phone", "Not provided"))


# Real-world style
users = {
    "101": {
        "name": "Aryan",
        "role": "developer"
    },
    "102": {
        "name": "Rahul",
        "role": "designer"
    }
}

for user_id, user in users.items():
    print(
        user_id,
        user.get("name"),
        user.get("role")
    )