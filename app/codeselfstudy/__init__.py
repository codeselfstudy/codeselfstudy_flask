from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from .views.pages import pages_bp


app = Flask(__name__, instance_relative_config=True)

# Import routes and logic for each section of the website from the views directory
app.register_blueprint(pages_bp)

# Database
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)
