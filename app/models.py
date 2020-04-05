# app/models.py

import os
import datetime
import hashlib
import humanfriendly

from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from sqlalchemy import CheckConstraint

class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    token = db.Column(db.String(255))
    admin = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.Boolean, nullable=False, default= 1)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Address(db.Model):
    __tablename__ = 'address'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    postal_code = db.Column(db.String(100))
    street = db.Column(db.String(100))
    number = db.Column(db.String(10))
    extra_details_address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Donor(db.Model):
    __tablename__ = 'donor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)
    
class Applicant(db.Model):
    __tablename__ = 'applicant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Dealer(db.Model):
    __tablename__ = 'dealer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    address = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class ProductType(db.Model):
    tablename = 'product_type'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Product(db.Model):
    __tablename__ = 'product'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_type_id = db.Column(db.Integer, db.ForeignKey('product_type.id'), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    image_url = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class StockDonor(db.Model):
    __tablename__ = 'stock_donor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)
    quantity = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class RequestApplicant(db.Model):
    __tablename__ = 'request_applicant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    quantitiy = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Journey(db.Model):
    __tablename__ = 'journey'
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    dealer_id = db.Column(db.Integer, db.ForeignKey('dealer.id'), nullable=False)
    initial_lat = db.Column(db.Float)
    initial_long = db.Column(db.Float)
    final_lat = db.Column(db.Float)
    final_long = db.Column(db.Float)
    valoration = db.Column(db.Float)
    status = db.Column(db.Integer, CheckConstraint('status IN (1, 2, 3)'))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)


class Package(db.Model):
    __tablename__ = 'package'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    journey_id = db.Column(db.Integer, db.ForeignKey('journey.id'), nullable=False)
    donor_id = db.Column(db.Integer, db.ForeignKey('donor.id'), nullable=False)
    applicant_id = db.Column(db.Integer, db.ForeignKey('applicant.id'), nullable=False)
    ts_pickup = db.Column(db.DateTime, nullable=True)
    ts_delivery = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.Integer, default = 0)
    package_valoration = db.Column(db.Float, nullable=True)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class PackageContent(db.Model):
    __tablename__ = 'package_content'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    package_id = db.Column(db.Integer, db.ForeignKey('package.id'), autoincrement=True)
    product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
    quantity = db.Column(db.Integer, default = 0)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)