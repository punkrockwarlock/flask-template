
import os
from flask import Flask, jsonify, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["DEBUG"] = True

# database config
SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://{username}:{password}@{hostname}/{databasename}".format(
    username="punkrockwarlock",
    password="michaela1",
    hostname="punkrockwarlock.mysql.pythonanywhere-services.com",
    databasename="punkrockwarlock$aFiN ",
)
app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_POOL_RECYCLE"] = 299
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20))
    email = db.Column(db.String(50))
    password = db.Column(db.String(50))

@app.route('/')
def home():
    google_key = os.environ["API_KEY"]
    return render_template("index.html", key=google_key)

@app.route('/register')
def register():
    pass
