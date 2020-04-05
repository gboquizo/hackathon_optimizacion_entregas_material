# app/modules/manager.py

import os

from app import db
from app.utils import upload_path, dd
from flask import render_template, Blueprint, request, flash, redirect, send_file, jsonify
from flask_login import login_required, current_user
from werkzeug.utils import secure_filename
from werkzeug.exceptions import abort

# Use modules for each logical domain
dealer_bp = Blueprint('dealer', __name__)

@dealer_bp.route('/map')
def index():
    print("Llega")
    
    return render_template('dealer/dealer.html', data={})
