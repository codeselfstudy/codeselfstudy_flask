from flask import Blueprint, render_template, redirect, url_for, flash
from ..forms import PostForm
from ..models.posts import Post

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    """Generates the index page of the application."""

    data = {}
    data['title'] = 'Code Self Study'
    data['leader_text'] = '''Elit recusandae modi vitae voluptatum nam praesentium, placeat blanditiis est aperiam eligendi ea odio deserunt! Veritatis placeat nesciunt voluptate natus cum, consequatur praesentium praesentium est maxime earum dolorem? Excepturi laborum.'''
    return render_template('pages/index.html', data=data)

@pages_bp.route('/forum/')
def forum_index():
    posts = []
    for post in Post.objects[:25].order_by('-created_at'):
        posts.append(post)
    data = {}
    data['title'] = 'Code Self Study Forum'
    data['posts'] = posts
    return render_template('forum/index.html', data=data)

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

@pages_bp.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data,
                    content=form.content.data,
                    published=True)
        post.save()
        submitted_data = (form.title.data, form.content.data)
        # TODO: pass in the type of alert to show: warning, default, etc.
        flash('Your post was saved!')
        # TODO: redirect to completed post, not the forum index
        return redirect('/forum/')

    data = {}
    data['title'] = 'Add New Post'
    return render_template('add_post.html', form=form, data=data)

