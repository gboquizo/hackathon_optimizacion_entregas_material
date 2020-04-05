# app/modules/manager.py

import os

from app import db
from app.models import User
from app.utils import upload_path, dd
from flask import render_template, Blueprint, request, flash, redirect, send_file, jsonify, url_for
from flask_login import login_required, current_user, login_user
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort
from app.forms import RegisterForm


# Use modules for each logical domain
donor_bp = Blueprint('donor', __name__)


@donor_bp.route('/register', methods=["POST"])
def register():
    """ User registration page."""
    register_form = RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate_on_submit():

        """
        existing_user = User.query.filter_by(email=register_form.email.data).first()

        # Register user
        call auth method
        
        if existing_user is None:
            user = User(
                email=request.form.get('email'),
                password=request.form.get('password'),
                username=request.form.get('username')
            )
            db.session.add(user)
            db.session.commit()
            login_user(user)
            return redirect(url_for('manager.index'))

        flash('A user already exists with that email address')
        return redirect(url_for('auth.register'))
        """
        donor = Donor()
        fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
        fk_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
        created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
        updated_at = db.Column(db.DateTime, nullable=True)

    return render_template('auth/register.html', title='Create an Account | ', form=register_form)
