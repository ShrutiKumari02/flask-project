# models.py

class Student:
    def __init__(self, student_id, name, age, email):
        self.id = student_id
        self.name = name
        self.age = age
        self.email = email

# Dictionary to store students in memory with ID as the key
students = {}
next_id = 1  # Helper variable to generate unique student IDs
