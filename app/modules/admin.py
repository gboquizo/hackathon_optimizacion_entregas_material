# Blueprint Configuration
from flask import Blueprint, render_template
from flask_login import current_user
from werkzeug.exceptions import abort

from app.models import User

admin_bp = Blueprint('admin', __name__)


@admin_bp.route('/admin-panel')
def index():
    if not current_user.is_admin():
        abort(403)
    users = User.query.all()
    return render_template('admin/index.html', users=users)
