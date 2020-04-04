# app/models.py

import os
import datetime
import hashlib
import humanfriendly

from werkzeug import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db

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
    city = db.Column(db.Integer, primary_key=True, autoincrement=True)
    postal_code = db.Column(db.String(100))
    street = db.Column(db.String(100))
    number = db.Column(db.String(10))
    extra_details_address = db.Column(db.String(255))
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Donor(db.Model):
    __tablename__ = 'donor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fk_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)
    
class Applicant(db.Model):
    __tablename__ = 'applicant'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fk_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class Dealer(db.Model):
    __tablename__ = 'dealer'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    fk_user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fk_address_id = db.Column(db.Integer, db.ForeignKey('address.id'), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, nullable=True)

class ProductType(db.Model):
    __tablename__ = 'product_type'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Product(db.Model):
    __tablename__ = 'product'
    DESCRIPCION
    IMAGE_URL

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class StockDonor(db.Model):
    __tablename__ = 'stock_donor'
    FOREIGNKEY PRODUCT
    FOREIGN KEY Donor
    INT CANTIDAD

class RequestApplicant(db.Model):
    __tablename__ = 'request_applicant'
    FOREIGNKEY PRODUCT
    FOREIGN KEY Applicant
    INT CANTIDAD

class Journey(db.Model):
    __tablename__ = 'journey'
    FOREIGN_KEY DEALER
    latitude initial
    longitude initial
    latitude final
    longitude final
    status 0 waiting 1 active 2 finished
    valoration journey

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

class Package(db.Model):
    __tablename__ = 'package'
    FOREIGN_KEY JOURNEY
    FOREIGN_KEY DONOR
    FOREIGN_KEY APPLICANT
    timestamp recogida
    timestamp entrega
    status 0 waiting 1 active 2 finished
    valoration package(donor)
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    
class PackageContent(db.Model):
    __tablename__ = 'package_content'
    package id 23 23
    product id 2 3
    cantidad 2 1
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)


"""     def __init__(self, filename):
        self.name = filename
        self.file = self.extract_file(filename)
        self.hash = self.extract_hash()
        self.created_at = datetime.datetime.now()
        self.size = self.calculate_size()

    def extract_file(self, filename):
        directory = os.getenv('UPLOAD_FOLDER', 'uploads')
        return os.path.join(directory, filename)

    def extract_hash(self):
        with open(self.file, "rb") as f:
            return hashlib.sha256(f.read()).hexdigest()

    def calculate_size(self):
        try:
            return humanfriendly.format_size(os.path.getsize(self.file))
        except os.error:
            print('There was a problem with the size of the file')

    def __repr__(self):
        return '<File {0}>'.format(self.name)
 """