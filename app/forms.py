from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, Length


class LoginForm(FlaskForm):
    """User Login Form."""
    email = StringField('Correo electrónico', validators=[
        Email('Por favor, introduce un correo electrónico válido.'),
        DataRequired('Por favor, introduce un correo.')
    ])
    password = PasswordField('Contraseña', validators=[DataRequired('Oh, ¿y la contraseña?')])
    remember_me = BooleanField('Recuérdame')
    submit = SubmitField('Entrar')


class RegisterForm(FlaskForm):
    """User Register Form."""
    email = StringField('Email', validators=[
        Email('Por favor, introduce un correo electrónico válido.'),
        DataRequired('Por favor, introduce un correo.')
    ])
    username = StringField('Nombre de usuario', validators=[DataRequired('¡Introduce un nombre de usuario!')])
    password = PasswordField('Contraseña', validators=[
        DataRequired('Por favor, introduzca una contraseña.'),
        Length(min=8, message='La contraseña tiene que ser más fuerte. Al menos 8 caracteres.'),
        EqualTo('password_confirm', message='Las contraseñas tienen que coincidir')
    ])
    password_confirm = PasswordField('Confirma tu contraseña')
    submit = SubmitField('Registrarme')
