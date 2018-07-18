from django.contrib.auth.models import User
from django.db import models
from web import settings

from taxonomy.models import Term

class MentoringInfo(models.Model):
    mentor = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    mentoring_field = models.ManyToManyField(Term, related_name='mentoring_field', blank=True)


class LearningInfo(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    learning_field = models.ManyToManyField(Term, related_name='learning_field', blank=True)
