from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

#initializing the app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}}, methods=["GET", "POST", "OPTIONS"], allow_headers=["Content-Type", "Access-Control-Allow-Origin"])

# configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# configure bcrypt (used for encrypting passwords)
bcrypt = Bcrypt(app)

if __name__ == "__main__":
    app.run(debug=True)