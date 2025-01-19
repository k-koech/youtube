from flask import Blueprint, jsonify
user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users")
def users():
    return jsonify({"users":"users"}), 200