from flask import Blueprint, render_template, redirect, url_for
from ..forms import PostForm
from ..models.post import Post

pages_bp = Blueprint('pages', __name__)

@pages_bp.route('/')
def index():
    """Generates the index page of the application."""
    posts = []
    for post in Post.objects:
        posts.append(post)
    data = {}
    data['title'] = 'Code Self Study'
    data['leader_text'] = posts
    return render_template('index.html', data=data)

@pages_bp.route('/about/')
def about():
    """Generates the about page."""
    data = {}
    data['title'] = 'About CodeSelfStudy.com'
    return render_template('about.html', data=data)

@pages_bp.route('/add-post', methods=['GET', 'POST'])
def add_post():
    form = PostForm()
    if form.validate_on_submit():
        print(dir(form))
        #post = 
        print(form.title, form.content)
        post = Post(title=form.title, content=form.content)
        post.save()
        return redirect('/')
    else:
        data = {}
        data['title'] = 'Add New Post'
        return render_template('add_post.html', form=form, data=data)

