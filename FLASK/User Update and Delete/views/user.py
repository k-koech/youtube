from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
from flask_jwt_extended import jwt_required, get_jwt_identity
from models import User, db

user_bp = Blueprint("user_bp", __name__)


@user_bp.route("/users", methods=["POST"])
def register_user():
    data = request.get_json()
    username = data["username"]
    email = data["email"]
    password = generate_password_hash( data["password"] )

    check_username = User.query.filter_by(username=username).first()
    check_email = User.query.filter_by(email=email).first()
    
    if check_username or check_email:
        return jsonify({"error":"Username/Email exists!"})
    
    else:
        new_user = User(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success":"User saved successfully!"}), 201
    
# Update user
@user_bp.route("/users", methods=["PATCH"])
@jwt_required()
def update_user():
    curent_user_id = get_jwt_identity()
    
    user = User.query.get(curent_user_id)

    if user:
        data = request.get_json()

        username = data.get("username", user.username)
        email = data.get("email", user.email)
        password = generate_password_hash( data.get("password", user.password) )

        check_username = User.query.filter_by(username=username and id!=user.id).first()
        check_email = User.query.filter_by(email=email and id!=user.id).first()
        
        if check_username or check_email:
            return jsonify({"error":"Username/Email exists!"})
        else:
            user.username = username
            user.email = email
            user.password = password

            db.session.commit()
            return jsonify({"success":"Profile updated successfully!"}), 201
    else:
        return jsonify({"error":"User doesn't exist"}),404

# Delete
@user_bp.route("/users", methods=["DELETE"])
@jwt_required()
def delete_useR():
    curent_user_id = get_jwt_identity()
    
    user = User.query.get(curent_user_id)

    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({"success":"Your account is deleted!"}), 200
    
    else:
        return jsonify({"error":"User doesn't exist"}),404
