from flask_wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from .models.post import Post

from flask_pagedown.fields import PageDownField
from wtforms.fields import SubmitField

class PageDownFormExample(Form):
    pagedown = PageDownField('Enter your markdown')
    submit = SubmitField('Submit')
# Manual example:
class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content = PageDownField('Content', validators=[DataRequired()])
    submit = SubmitField('Publish')
