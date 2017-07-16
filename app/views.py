from flask import render_template, redirect, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user

from . import app
from . import db
from .models import User
from .forms import RegisterForm, LoginForm

@app.route('/')
@app.route('/index')
def home():
    google_key = app.config["GOOGLE_API_KEY"]
    return render_template("index.html", key=google_key)

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

@app.route('/register', methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        user = User()
        user.email = form.email.data
        user.password = form.password.data
        db.session.add(user)
        db.session.commit()
        flash("Registered successfully")
        return redirect(url_for('login'))

    return render_template('register.html', form=form)

@app.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first_or_404()

        if user.is_correct_password(form.password.data):
            login_user(user)

            return redirect(url_for('home'))
        else:
            return redirect(url_for('register'))

    return render_template('login.html', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash("Logged out")

    return redirect(url_for('home'))
