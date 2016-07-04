from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=140)
    age = models.CharField(max_length=140)
    description = models.TextField()
    user = models.ForeignKey(User)

    def __str__(self):
		return self.name
