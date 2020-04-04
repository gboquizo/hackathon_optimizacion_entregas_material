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
    email = db.Column(db.String(255), unique=True)
    username = db.Column(db.String(255), unique=True, nullable=True)
    password = db.Column(db.String(255), nullable=False)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    status = db.Column(db.Boolean, nullable=False, default=True)
    updated_at = db.Column(db.DateTime, nullable=True)
    created_at = db.Column(db.DateTime, nullable=True)
    files = db.relationship('File', backref='uploaded', lazy='dynamic')

    def __init__(self, email, password, username, admin=False):
        self.username = username
        self.email = email
        self.set_password(password)
        self.created_at = datetime.datetime.now()
        self.admin = admin

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def is_active(self):
        return self.status

    def is_admin(self):
        return self.admin

    def __repr__(self):
        return '<User {0}>'.format(self.email)


class File(db.Model):
    __tablename__ = 'files'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), unique=True, nullable=True)
    hash = db.Column(db.String(64), nullable=True)
    size = db.Column(db.String(255), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, filename):
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
