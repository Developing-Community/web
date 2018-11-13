from django.db import models


# Create your models here.


class Application(models.Model):
    title = models.CharField(max_length=255)
    API_TOKEN = models.CharField(max_length=255, null=True, blank=True)
