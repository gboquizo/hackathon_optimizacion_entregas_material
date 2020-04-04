from flask import Flask
import uuid

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

app = Flask(__name__)
app.config.from_pyfile('config.cfg') ESTO ANDANDA?
db = SQLAlchemy(app)

migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('health_material', MigrateCommand)

class User(db.Model):
    id = db.Column(db.uuid, primary_key=True)
    name = db.Column(db.String(30))


class Application(db.Model):
    id = db.Column(db.uuid, primary_key=True)

class Donor(db.Model):
    id = db.Column(db.uuid, primary_key=True)

class Dealer(db.Model):
    id = db.Column(db.uuid, primary_key=True)
