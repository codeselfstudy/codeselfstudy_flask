from flask.ext.wtf import Form
from wtforms.fields import TextField, TextAreaField
from wtforms import validators 
from .models.post import Post

# Manual example:
class PostForm(Form):
    title = TextField('Title', [validators.required(),
                                validators.length(max=120)])
    content = TextAreaField('Content', [validators.required()])

