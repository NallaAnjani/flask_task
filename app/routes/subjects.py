from flask import Blueprint, request, jsonify
from app import db
from app.models import Subject

subjects_bp = Blueprint("subjects", __name__)

@subjects_bp.route("/", methods=["POST"])
def add_subject():
    data = request.json
    if "name" not in data:
        return jsonify({"error": "Name required"}), 400

    if Subject.query.filter_by(name=data["name"]).first():
        return jsonify({"error": "Subject already exists"}), 400

    new_subject = Subject(name=data["name"])
    db.session.add(new_subject)
    db.session.commit()
    return jsonify({"message": "Subject added"}), 201

@subjects_bp.route("/", methods=["GET"])
def get_subjects():
    subjects = Subject.query.all()
    return jsonify([{"id": s.id, "name": s.name} for s in subjects]), 200
