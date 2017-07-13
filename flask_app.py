
from flask import Flask, jsonify, render_template, request, url_for

app = Flask(__name__)

@app.route('/')
def home():
    google_key = "AIzaSyCNbSdyHpGFWjSarkPVIWHZV7dAoGVIYoY"
    return render_template("index.html", key=google_key)

@app.route('/register')
def register():

