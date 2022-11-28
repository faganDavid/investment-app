from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length, Optional


class SignUpForm(FlaskForm):
    """User Sign up form"""
    name = StringField(
        'Name',
        validators=[DataRequired()
        ]
    )
    email = StringField(
        'Email',
        validators=[
            Length(min=6),
            Email(message="Enter a valid email."),
            DataRequired()
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired(),
            Length(min=6, message="Select a stronger password.")
        ]
    )
    confirm = PasswordField(
        'Confirm Password',
        validators=[
            DataRequired(),
            Length(min=6, message="Passwords must match.")
        ]
    )


class LoginForm(FlaskForm):
    """User log in form"""
    email = StringField(
        'Email',
        validators=[
            DataRequired(),
            Email(message="Enter a valid email.")
        ]
    )
    password = PasswordField(
        'Password',
        validators=[
            DataRequired()
        ]
    )
    submit = SubmitField(
        'Login'
    )
