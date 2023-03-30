from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Access-Control-Allow-Origin"])
app.secret_key = 'zoomie-roomie' #needs to be changed to something more secure


# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



from .views import *
from .models import *

with app.app_context():
    db.create_all()
