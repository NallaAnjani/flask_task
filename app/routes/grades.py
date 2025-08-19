from flask import Blueprint, request, jsonify
from app import db
from app.models import Grade, Student, Subject
from sqlalchemy.sql import func

grades_bp = Blueprint("grades", __name__)

# POST grade
@grades_bp.route("/", methods=["POST"])
def add_grade():
    data = request.json
    student = Student.query.get(data.get("student_id"))
    subject = Subject.query.get(data.get("subject_id"))

    if not student or not subject:
        return jsonify({"error": "Invalid student or subject"}), 400

    new_grade = Grade(student_id=student.id, subject_id=subject.id, grade=data["grade"])
    db.session.add(new_grade)
    db.session.commit()
    return jsonify({"message": "Grade added"}), 201

# Get all grades for a student
@grades_bp.route("/student/<int:student_id>", methods=["GET"])
def get_student_grades(student_id):
    grades = Grade.query.filter_by(student_id=student_id).all()
    return jsonify([{"subject_id": g.subject_id, "grade": g.grade} for g in grades]), 200

# Get all grades for a subject
@grades_bp.route("/subject/<int:subject_id>", methods=["GET"])
def get_subject_grades(subject_id):
    grades = Grade.query.filter_by(subject_id=subject_id).all()
    return jsonify([{"student_id": g.student_id, "grade": g.grade} for g in grades]), 200

# Update grade
@grades_bp.route("/<int:grade_id>", methods=["PUT"])
def update_grade(grade_id):
    data = request.json
    grade = Grade.query.get(grade_id)
    if not grade:
        return jsonify({"error": "Grade not found"}), 404

    grade.grade = data.get("grade", grade.grade)
    db.session.commit()
    return jsonify({"message": "Grade updated"}), 200

# Reports
@grades_bp.route("/student/<int:student_id>/average", methods=["GET"])
def student_average(student_id):
    avg = db.session.query(func.avg(Grade.grade)).filter(Grade.student_id == student_id).scalar()
    return jsonify({"student_id": student_id, "average": avg}), 200

@grades_bp.route("/subject/<int:subject_id>/class-average", methods=["GET"])
def subject_average(subject_id):
    avg = db.session.query(func.avg(Grade.grade)).filter(Grade.subject_id == subject_id).scalar()
    return jsonify({"subject_id": subject_id, "class_average": avg}), 200

@grades_bp.route("/student/<int:student_id>/report-card", methods=["GET"])
def report_card(student_id):
    grades = Grade.query.filter_by(student_id=student_id).all()
    result = [{"subject_id": g.subject_id, "grade": g.grade} for g in grades]
    avg = db.session.query(func.avg(Grade.grade)).filter(Grade.student_id == student_id).scalar()
    return jsonify({"student_id": student_id, "grades": result, "average": avg}), 200
