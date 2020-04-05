# app/modules/manager.py

import os

from app import db
from app.utils import dd
from flask import render_template, Blueprint, request, flash, redirect, send_file, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

# Use modules for each logical domain
manager_bp = Blueprint('manager', __name__)

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}


def allowed_files(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@manager_bp.route('/index')
@manager_bp.route('/')
def index():
    return render_template('manager/index.html', title='Index')


@manager_bp.route('/my-files')
@manager_bp.route('/files/<username>')
@login_required
def show(username=None):
    user = User.query.filter_by(id=username).first()

    if user is None:
        user = current_user

    if user is not current_user and not current_user.is_admin():
        abort(404)

    path = upload_path()

    return render_template('manager/show.html', title=user.username + ' files', user=user, path=path)


@manager_bp.route('/upload-file', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            flash('No file selected for uploading')
            return redirect(request.url)

        if file and allowed_files(file.filename):
            filename = secure_filename(file.filename)
            directory = upload_path()

            file.save(os.path.join(directory, filename))
            database_file = File(file.filename)

            if File.query.filter_by(hash=database_file.hash).first() is None:
                current_user.files.append(database_file)
                db.session.add(database_file)
                db.session.commit()
                flash('File successfully uploaded')
            else:
                flash('This file is already exists')

            return redirect('/upload-file')

        else:
            flash('Allowed file types are txt, pdf, png, jpg, jpeg and gif')
            return redirect(request.url)

    return render_template('main/upload-form.html')


@manager_bp.route('/files/download/<filename>')
@login_required
def download(filename):
    file = File.query.filter_by(name=filename).first()

    if file is None:
        abort(404)

    return send_file(os.path.join(upload_path(), file.name), as_attachment=True)


@manager_bp.route('/files/delete/<identifier>', methods=['DELETE'])
@login_required
def destroy(identifier):
    file = File.query.filter_by(id=identifier).first()

    if file is None:
        abort(404)

    filename = file.name

    os.remove(os.path.join(upload_path(), filename))

    db.session.delete(file)
    db.session.commit()

    return jsonify(success=True, message='File ' + filename + ' was deleted successfully')
