from flask import Blueprint, jsonify, request
from werkzeug.security import generate_password_hash
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
        return jsonify({"success":"User saved successfully!"}), 200