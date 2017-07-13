from flask import render_template, redirect, url_for, flash

from . import app
from . import db
from .models import User
from .forms import EmailPasswordForm

@app.route('/')
def home():
    google_key = app.config["GOOGLE_API_KEY"]
    return render_template("index.html", key=google_key)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = EmailPasswordForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
        return redirect(url_for('/register'))

    return render_template('register.html', form=form)

