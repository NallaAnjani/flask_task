from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required

auth_bp = Blueprint("auth", __name__)

USERS = {"admin": "password123"}  # demo user

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json
    if data["username"] in USERS and USERS[data["username"]] == data["password"]:
        token = create_access_token(identity=data["username"])
        return jsonify(access_token=token), 200
    return jsonify({"error": "Invalid credentials"}), 401

@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    return jsonify({"message": "You accessed a protected route!"}), 200
