import mongoengine as me
from .base import ContentNode

# monod --> pymongo --> (monoengine!) ... could have also used ...> mongoalchemy|mongokit
# but mongoengine was more popular
# nerdcommenter vi commenting plugin

# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class ForumPost(ContentNode):
    category = me.StringField()
    comments_allowed = me.BooleanField(default=True, required=True)
