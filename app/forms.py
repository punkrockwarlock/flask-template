from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from .validators import Unique
from .models import User

class RegisterForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(),
    Unique(User, User.email, message="Email already registered.")])
    password = PasswordField('Password', validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField(label='Submit')

class LoginForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField(label='Submit')