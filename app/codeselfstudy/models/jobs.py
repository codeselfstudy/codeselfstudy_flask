import datetime
import mongoengine as me
from .base import ContentNode


class Job(ContentNode):
    expiration_date = me.DateTimeField(required=True)
    company = me.StringField(required=True)
    # TODO: add more fields
