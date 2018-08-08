from enum import Enum
from django.db import models
from django.utils import timezone

from companions.models import Application
from taxonomy.models import Term
from web import settings


def content_image_upload_location(instance, filename):
    x = timezone.now()
    return "%s/%s/%s/%s" % (x.year, x.month, x.day, filename)


class ContentType(Enum):  # A subclass of Enum
    ARTICLE = "article"
    REPORT = "report"
    PROBLEM = "problem"
    COMMENT = "comment"


class Content(models.Model):  # We want comment to have a foreign key to all contents so we use all of them as one
    title = models.CharField(max_length=255)
    type = models.CharField(
        max_length=30,
        choices=[(tag, tag.value) for tag in ContentType]  # Choices is a list of Tuple
    )
    application = models.ForeignKey(Application, default=1, null=True, on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True, blank=True, null=True)
    subject = models.ForeignKey(Term, related_name="subject", blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=content_image_upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    note = models.TextField(null=True, blank=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    read_time = models.IntegerField(default=0)  # models.TimeField(null=True, blank=True) #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
    terms = models.ManyToManyField(Term, related_name="terms", blank=True)
    def __str__(self):
        return self.title


class ContentRealtionType(Enum):  # A subclass of Enum
    COMMENTED_ON = "commented_on"


class ContentRelation(models.Model):
    source = models.ForeignKey(Content, related_name='source', on_delete=models.CASCADE)
    destination = models.ForeignKey(Content, related_name='destination', on_delete=models.CASCADE)
    type = models.CharField(
        max_length=30,
        choices=[(tag, tag.value) for tag in ContentRealtionType]  # Choices is a list of Tuple
    )
