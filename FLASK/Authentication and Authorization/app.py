from flask import Flask
from models import db
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from datetime import timedelta

app = Flask(__name__)

# migration initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
migrate = Migrate(app, db)
db.init_app(app)

# configure jwt
jwt = JWTManager(app)
jwt.init_app(app)

app.config["JWT_SECRET_KEY"] = "jkgfhtygvbhljnjn"
app.config["JWT_ACCESS_TOKEN_EXPIRES"]= timedelta(hours=2)

from views import *
app.register_blueprint(user_bp)
app.register_blueprint(todo_bp)
app.register_blueprint(auth_bp)
app.register_blueprint(tag_bp)


@jwt.token_in_blocklist_loader
def check_if_token_revoked(jwt_header, jwt_payload: dict) -> bool:
    jti = jwt_payload["jti"]
    token = db.session.query(TokenBlocklist.id).filter_by(jti=jti).scalar()

    return token is not None