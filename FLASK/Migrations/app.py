from flask import Flask
from models import db
from flask_migrate import Migrate
app = Flask(__name__)

# migration initialization
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
migrate = Migrate(app, db)

db.init_app(app)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"