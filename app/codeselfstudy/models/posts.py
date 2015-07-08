import datetime
import mongoengine as me

# monod --> pymongo --> (monoengine!) ... could have also used ...> mongoalchemy|mongokit
# but mongoengine was more popular


# Based on: https://flask-mongoengine.readthedocs.org/en/latest/

class Comment(me.EmbeddedDocument):
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    body = me.StringField(verbose_name="Comment", required=True)

class Post(me.Document):
    title = me.StringField(max_length=120, required=True)
    created_at = me.DateTimeField(default=datetime.datetime.now, required=True)
    content = me.StringField(required=True)
    published = me.BooleanField(required=True)
    slug = me.StringField(max_length=155, required=True)
    comments = me.ListField(me.EmbeddedDocumentField('Comment'))

    def get_absolute_url(self):
        return url_for('post', kwargs={'slug': self.slug})

    meta = {
        'allow_inheritance': True,
        'indexes': ['-created_at', 'slug'],
        'ordering': ['-created_at']
    }

    # TODO: make sure this is what we want. It's based on the MongoEngine docs.
    # Doesn't seem to work
    #@me.queryset_manager
    #def live_posts(doc_cls, queryset):
        #return queryset.filter(published=True)

