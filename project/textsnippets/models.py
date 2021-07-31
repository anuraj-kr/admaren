from django.db import models
from authentication.models import *
from django.contrib.auth.models import AbstractUser, User
from datetime import datetime as dt

class Tags(models.Model):

    TagId = models.AutoField(primary_key=True)
    Tag = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.Tag


class Textsnippet(models.Model):

    SnippetId = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    TagId = models.ForeignKey(Tags, on_delete=models.CASCADE, verbose_name='Tags', related_name='Textsnippet')
    Timestamp = models.DateTimeField(default=dt.now, null=True, blank=True)
    CreatedBy = models.ForeignKey('authentication.User', on_delete=models.CASCADE, verbose_name='User', related_name='Textsnippet')

    def __str__(self):
        return self.Title
