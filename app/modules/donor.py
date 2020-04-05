# app/modules/manager.py

import os

from app import db, ma
from app.utils import upload_path, dd
from flask import render_template, Blueprint, request, flash, redirect, send_file, jsonify, url_for
from flask_login import login_required, current_user, login_user
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

from app.forms import RegisterForm
from ..models import Address, Donor, User
from ..schemas import AddressSchema, DonorSchema

# Use modules for each logical domain
donor_bp = Blueprint('donor', __name__)


@donor_bp.route('/register', methods=["POST"])
def register():
    """ User registration page."""
    register_form = RegisterForm(request.form)

    if request.method == 'POST' and register_form.validate_on_submit():

        """
        # Register user
        call auth method
        
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
            return redirect(url_for('manager.index'))

        flash('A user already exists with that email address')
        return redirect(url_for('auth.register'))
        """
        json_data = request.get_json()
        if not json_data:
            return {"message": "No input data provided"}, 400

        # Register address
        # Validate and deserialize input
        try:
            address_data = AddressSchema(json_data)
        except ma.ValidationError as err:
            print(err.messages)
            return err.messages, 422

        address = Address(address_data)
        db.session.add(address)
        db.session.commit()
        id_address = AddressSchema().dump(Address.query.get(address.id))

        # register donor
        # Validate and deserialize input
        try:
            donor_data = DonorSchema(json_data)
            donor_data['address'] = id_address
        except ma.ValidationError as err:
            print(err.messages)
            return err.messages, 422

        donor = Donor(donor_data)
        db.session.add(donor)
        db.session.commit()
        id_donor = DonorSchema().dump(donor.query.get(donor.id))

    return {"message": "Donor user registered.", "id": id_donor}, 200
