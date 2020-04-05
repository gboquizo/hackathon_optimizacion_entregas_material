# app/__init__.py

import os

from flask import Flask, render_template
from flask_debugtoolbar import DebugToolbarExtension
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_wtf import CSRFProtect
from flask_marshmallow import Marshmallow

# Instantiate the extensions
db = SQLAlchemy()
ma = Marshmallow()
csrf = CSRFProtect()
login_manager = LoginManager()
migrate = Migrate()
toolbar = DebugToolbarExtension()


def create_app():
    app = Flask(__name__)

    # Set config
    #app_settings = os.getenv('APP_SETTINGS', 'app.config.ProductionConfig')
    app_settings = os.getenv('APP_SETTINGS', 'app.config.DevelopmentConfig')
    app.config.from_object(app_settings)

    # Set up extensions
    login_manager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)
    toolbar.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        from app.modules.auth import auth_bp
        from app.modules.admin import admin_bp
        from app.modules.dealer import dealer_bp
        from app.modules.donor import donor_bp
        app.register_blueprint(auth_bp)
        app.register_blueprint(admin_bp)
        app.register_blueprint(dealer_bp)
        app.register_blueprint(donor_bp)

        # Initialize Global db
        db.create_all()

    # Error handlers
    @app.errorhandler(403)
    def forbidden_page(error):
        return render_template('errors/403.html'), 403

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def server_error_page(error):
        return render_template('errors/500.html'), 500

    # shell context for flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app
