import datetime
from .. import db


# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class Content(db.EmbeddedDocument):
    text = db.StringField(required=True)

class Post(db.Document):
    title = db.StringField(max_length=120, required=True)
    created_at = db.DateTimeField(default=datetime.datetime.now, required=True)
    #author = db.ReferenceField(User)
    #tags = db.ListField(db.StringField(max_length=30))
    content = db.EmbeddedDocumentField(Content)

