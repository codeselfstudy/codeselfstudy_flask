from flask import Flask
from .views.pages import pages_bp


app = Flask(__name__)

# Import routes and logic for each section of the website from the views directory
app.register_blueprint(pages_bp)

