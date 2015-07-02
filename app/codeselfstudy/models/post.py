import datetime
import mongoengine as me


# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class Content(me.EmbeddedDocument):
    text = me.StringField(required=True)

class Post(me.Document):
    title = me.StringField(max_length=120, required=True)
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    #author = me.ReferenceField(User)
    #tags = me.ListField(me.StringField(max_length=30))
    content = me.EmbeddedDocumentField(Content)

