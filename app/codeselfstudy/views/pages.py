from flask import Blueprint, render_template


pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    """Generates the index page of the application."""
    data = {}
    data['title'] = 'Code Self Study'
    data['leader_text'] = "Welcome."
    return render_template('index.html', data=data)

@pages_bp.route('/about/')
def about():
    """Generates the about page."""
    data = {}
    data['title'] = 'About CodeSelfStudy.com'
    return render_template('about.html', data=data)
