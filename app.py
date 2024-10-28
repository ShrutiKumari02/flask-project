# app.py

from flask import Flask, jsonify, request
from models import Student, students, next_id

app = Flask(__name__)

# Helper function to increment the student ID
def get_next_id():
    global next_id
    student_id = next_id
    next_id += 1
    return student_id

# Route to create a new student
@app.route('/students', methods=['POST'])
def create_student():
    global students
    data = request.get_json()
    if not data or 'name' not in data or 'age' not in data or 'email' not in data:
        return jsonify({"error": "Invalid data"}), 400

    student = Student(get_next_id(), data['name'], data['age'], data['email'])
    students[student.id] = student
    return jsonify(student.__dict__), 201

# Route to get all students
@app.route('/students', methods=['GET'])
def get_students():
    return jsonify([student.__dict__ for student in students.values()])

# Route to get a student by ID
@app.route('/students/<int:student_id>', methods=['GET'])
def get_student(student_id):
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify(student.__dict__)

# Route to update a student by ID
@app.route('/students/<int:student_id>', methods=['PUT'])
def update_student(student_id):
    data = request.get_json()
    student = students.get(student_id)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    if 'name' in data:
        student.name = data['name']
    if 'age' in data:
        student.age = data['age']
    if 'email' in data:
        student.email = data['email']
    return jsonify(student.__dict__)

# Route to delete a student by ID
@app.route('/students/<int:student_id>', methods=['DELETE'])
def delete_student(student_id):
    student = students.pop(student_id, None)
    if not student:
        return jsonify({"error": "Student not found"}), 404
    return jsonify({"message": "Student deleted"}), 200

if __name__ == '__main__':
    app.run(debug=True)
