from flask_wtf import Form
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired
from flask_pagedown.fields import PageDownField
from .models.post import Post


class PostForm(Form):
    """Fields for the add-post form."""
    title = StringField('Title', validators=[DataRequired()])
    content = PageDownField('Content', validators=[DataRequired()])
    submit = SubmitField('Publish')
