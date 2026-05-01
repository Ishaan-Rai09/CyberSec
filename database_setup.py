from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os

app = Flask(__name__)
# Absolute path for the database
db_path = os.path.join(os.path.dirname(__file__), 'vault.db')
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_path}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ConfidentialUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    # These fields will store ENCRYPTED strings
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

class AuditLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, server_default=db.func.now())
    action = db.Column(db.String(255), nullable=False)
    user_identity = db.Column(db.String(255)) # Encrypted
    status = db.Column(db.String(50)) # Success/Failure

def init_db():
    with app.app_context():
        db.create_all()
        print("Database initialized with Confidential Tables.")

if __name__ == "__main__":
    init_db()
