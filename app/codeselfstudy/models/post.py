import datetime
import mongoengine as me


# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class Post(me.Document):
    title = me.StringField(max_length=120, required=True)
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    content = me.StringField(required=True)
    published = me.BooleanField(required=True)

    # TODO: make sure this is what we want. It's based on the MongoEngine docs.
    # Doesn't seem to work
    #@me.queryset_manager
    #def live_posts(doc_cls, queryset):
        #return queryset.filter(published=True)

