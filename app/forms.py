from flask_wtf import Form
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo

from .validators import Unique
from .models import User

class EmailPasswordForm(Form):
    email = StringField('Email', validators=[DataRequired(), Email(),
        Unique(
            User,
            User.email,
            message="There is already an account with that email")])
    password = PasswordField('Password', validators=[DataRequired(),
        EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Repeat Password')
    submit = SubmitField(label='Submit')