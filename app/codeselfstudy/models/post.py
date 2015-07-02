import datetime
import mongoengine as me


# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class Post(me.Document):
    title = me.StringField(max_length=120, required=True)
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    content = me.StringField(required=True)

