from flask.ext.wtf import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired
from .models.post import Post

# Manual example:
class PostForm(Form):
    title = StringField('Title', validators=[DataRequired()])
    content = TextAreaField('Content', validators=[DataRequired()])

