from flask import Blueprint, render_template, redirect, url_for, flash
from ..models.pages import Page

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    """Generates the index page of the application."""

    data = {}
    data['title'] = 'Code Self Study'
    data['leader_text'] = '''Elit recusandae modi vitae voluptatum nam praesentium, placeat blanditiis est aperiam eligendi ea odio deserunt! Veritatis placeat nesciunt voluptate natus cum, consequatur praesentium praesentium est maxime earum dolorem? Excepturi laborum.'''
    return render_template('pages/index.html', data=data)

@pages_bp.route('/about/')
def about():
    """Generates the about page."""
    data = {}
    data['title'] = 'About CodeSelfStudy.com'
    return render_template('pages/about.html', data=data)

@pages_bp.route('/edu/')
def edu():
    """Generates the /edu/ page."""\
    # TODO: get the content from the database
    data = {'title': 'Edu'}
    return render_template('pages/edu.html', data=data)

@pages_bp.route('/events/')
def events():
    """Generates the /edu/ page.""" \
        # TODO: get the content from the database
    data = {'title': 'Events'}
    return render_template('pages/events.html', data=data)

