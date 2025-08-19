from flask import Blueprint, request, jsonify
from app import db
from app.models import Teacher

teachers_bp = Blueprint("teachers", __name__)

@teachers_bp.route("/", methods=["POST"])
def add_teacher():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Name required"}), 400

    if Teacher.query.filter_by(name=data["name"]).first():
        return jsonify({"error": "Teacher already exists"}), 400

    new_teacher = Teacher(name=data["name"])
    db.session.add(new_teacher)
    db.session.commit()
    return jsonify({"message": "Teacher added"}), 201

@teachers_bp.route("/", methods=["GET"])
def get_teachers():
    teachers = Teacher.query.all()
    return jsonify([{"id": t.id, "name": t.name} for t in teachers]), 200
