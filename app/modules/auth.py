# app/modules/auth.py

"""Routes for user authentication."""
from app import login_manager, db
from app.forms import LoginForm, RegisterForm
from app.models import User
from flask import render_template, redirect, flash, url_for, Blueprint, request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse

# Blueprint Configuration
auth_bp = Blueprint('auth', __name__)


# Middleware to authorization
@login_manager.unauthorized_handler
def unauthorized():
    """Redirect unauthorized users to Login page."""
    return redirect(url_for('auth.login'))


# Middleware to check if a user is authenticated.
@login_manager.user_loader
def load_user(user_id):
    """Check if auth is logged-in on every page load."""
    if user_id is not None:
        return User.query.get(user_id)

    return None

@auth_bp.route('/index')
@auth_bp.route('/')
def index():
    return render_template('auth/index.html', title='Index')

# Route to register a user.
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """ User registration page."""
    register_form = RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate_on_submit():
        existing_user = User.query.filter_by(email=register_form.email.data).first()

        if existing_user is None:
            user = User(
                email=request.form.get('email'),
                password=request.form.get('password'),
                username=request.form.get('username')
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('auth.index'))

        flash('A user already exists with that email address')
        return redirect(url_for('auth.register'))

    return render_template('auth/register.html', title='Create an Account | ', form=register_form)


# Route to sign in a user.
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """ User login page."""
    if current_user.is_authenticated:
        return redirect(url_for('auth.index'))

    login_form = LoginForm(request.form)

    if request.method == 'POST' and login_form.validate_on_submit():
        user = User.query.filter_by(email=login_form.email.data).first()

        if user is None or not user.check_password(login_form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('auth.login'))

        login_user(user, remember=login_form.remember_me.data)
        next_page = request.args.get('next')

        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('auth.show')

        return redirect(next_page)

    return render_template('auth/login.html', title='Sign in | ', form=login_form)


# Route to logout a user.
@auth_bp.route('/logout')
@login_required
def logout():
    """User logout logic."""
    logout_user()
    return redirect(url_for('auth.index'))
