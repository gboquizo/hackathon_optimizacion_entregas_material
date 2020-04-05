# app/config.py

import os

basedir = os.path.abspath(os.path.dirname(__file__))


class BaseConfig(object):
    """Base configuration."""
    APP_NAME = os.getenv('APP_NAME', 'Manager')
    BCRYPT_LOG_ROUNDS = 4
    DEBUG_TB_ENABLED = False
    SECRET_KEY = os.getenv('SECRET_KEY', 'secret_key')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False


class DevelopmentConfig(BaseConfig):
    """Development configuration."""
    DEBUG_TB_ENABLED = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{0}'.format(
        os.path.join(basedir, 'dev.sqlite')
    )


class TestingConfig(BaseConfig):
    """Testing configuration."""
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///'
    TESTING = True


class ProductionConfig(BaseConfig):
    """Production configuration."""
    DB_NAME = os.getenv('PSQL_DB_NAME', 'example')
    DB_USER = os.getenv('PSQL_DB_USER', 'postgres')
    DB_PASSWD = os.getenv('PSQL_DB_PASSWD', '')
    BCRYPT_LOG_ROUNDS = 13
    SQLALCHEMY_DATABASE_URI = 'postgresql://{0}:{1}@localhost/{2}'.format(DB_USER, DB_PASSWD, DB_NAME)
    WTF_CSRF_ENABLED = True