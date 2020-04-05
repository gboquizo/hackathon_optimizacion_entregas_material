from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    """User Login Form."""
    email = StringField('Email', validators=[
        Email('Please enter a valid email address.'),
        DataRequired('Please enter a valid email address.')
    ])
    password = PasswordField('Password', validators=[DataRequired('Uhh, your password tho?')])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign in')


class RegisterForm(FlaskForm):
    """User Register Form."""
    email = StringField('Email', validators=[
        Email('Please enter a valid email address.'),
        DataRequired('Please enter a valid email address.')
    ])
    username = StringField('Username', validators=[DataRequired('Enter a fake name or something.')])
    password = PasswordField('Password', validators=[
        DataRequired('Please enter a password.'),
        Length(min=8, message='Please select a stronger password'),
        EqualTo('password_confirm', message='Password must match')
    ])
    password_confirm = PasswordField('Confirm your Password')
    submit = SubmitField('Register')
