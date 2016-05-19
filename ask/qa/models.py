from __future__ import unicode_literals

from django.db import models


class User(models.Model):
    login = models.CharField(unique=True, max_length=50)
    password = models.CharField(max_length=50)
    name = models.CharField(max_length=50)


class Session(models.Model):
    key = models.CharField(unique=True, max_length=50)
    user = models.ForeignKey(User, default=1)
    expires = models.DateTimeField()


class Question(models.Model):
    title = models.CharField(max_length=50)
    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=1)
    author = models.ForeignKey(User, default=1)
    likes = models.ManyToManyField(User, related_name='likes_set')

    def get_url(self):
        return '/question/%d/' % self.pk

    class Meta:
        db_table = 'question'


class Answer(models.Model):

    text = models.TextField()
    added_at = models.DateTimeField(auto_now_add=True)
    question = models.ForeignKey(Question, default=1)
    author = models.ForeignKey(User, default=1)

    def __unicode__(self):
        return self.text

    def get_url(self):
        return '/answer/%d/' % self.pk

    class Meta:
        db_table = 'answer'

