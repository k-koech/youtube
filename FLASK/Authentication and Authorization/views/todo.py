from flask import Blueprint, jsonify

todo_bp = Blueprint("todo_bp", __name__)


@todo_bp.route("/todos")
def todos():
    return jsonify({"todos":"Todos list"}), 200