from flask import Blueprint, request, jsonify
from app import db
from app.models import Student

students_bp = Blueprint("students", __name__)

@students_bp.route("/", methods=["POST"])
def add_student():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Name required"}), 400
    
    new_student = Student(name=data["name"])
    db.session.add(new_student)
    db.session.commit()
    return jsonify({"message": "Student added successfully"}), 201

@students_bp.route("/", methods=["GET"])
def get_students():
    students = Student.query.all()
    result = [{"id": s.id, "name": s.name} for s in students]
    return jsonify(result), 200
