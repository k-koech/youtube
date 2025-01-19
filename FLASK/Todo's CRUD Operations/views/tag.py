from flask import Blueprint, jsonify, request
from models import Tag, db
tag_bp = Blueprint("tag_bp", __name__)


@tag_bp.route("/tags", methods=["POST"])
def add_tag():
    data = request.get_json()
    name = data["name"]
    
    check_name = Tag.query.filter_by(name=name).first()
    if check_name:
        return jsonify({"error":"Tags ex!ist"}), 406
    
    else:
        new_tag = Tag(name=name)
        db.session.add(new_tag)
        db.session.commit()

        return jsonify({"success":"Tag added"}), 201

# update tag
@tag_bp.route("/tags/<int:tag_id>", methods=["PATCH"])
def update_tag(tag_id):
    data = request.get_json()
    name = data["name"]
    
    tag = Tag.query.get(tag_id)
    if tag:
        check_name = Tag.query.filter_by(name=name).first()

        if check_name:
            jsonify({"error":"Tags exist"}), 406
        
        else:
            tag.name=name
            db.session.commit()

            return jsonify({"success":"Tag updated"}), 201
    else:
        return jsonify({"error":"Tag doesn't exist!"}), 404

# delete
@tag_bp.route("/tags/<int:tag_id>", methods=["DELETE"])
def dlete_tag(tag_id):
    tag = Tag.query.get(tag_id)
    if tag:
        db.session.delete(tag)
        db.session.commit()
        return jsonify({"success":"Tag deleted"}), 200
    else:
        return jsonify({"error":"Tag doesn't exist!"}), 404