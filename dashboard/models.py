from __future__ import unicode_literals

from django.db import models
from django.conf import settings


class Tag(models.Model):

    tag = models.CharField(max_length=100)

    def __unicode__(self):
        return self.tag


class Bookmark(models.Model):

    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    title = models.CharField(max_length=30, null=False)
    link = models.CharField(max_length=300, null=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return self.title


class BookmarkTag(models.Model):

    bookmark = models.ForeignKey(Bookmark, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag)
    created = models.DateTimeField(auto_now_add=True)

    def get_count(self):
        return BookmarkTag.objects.filter(tag=self.tag).count()


    def __unicode__(self):
        return self.tag.tag