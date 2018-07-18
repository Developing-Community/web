from django.db import models
from web import settings

from taxonomy.models import Term

class MentoringInfo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    learning_field = models.ManyToManyField(Term, related_name='mentoring_field', blank=True)


class LearningInfo(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    learning_field = models.ManyToManyField(Term, related_name='learning_field', blank=True)
