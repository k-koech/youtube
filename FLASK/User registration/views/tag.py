from flask import Blueprint, jsonify

tag_bp = Blueprint("tag_bp", __name__)


@tag_bp.route("/tags")
def tags():
    return jsonify({"tags":"Tags list"}), 200