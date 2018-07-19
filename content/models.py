from enum import Enum
from django.db import models
from django.utils import timezone

from web import settings

def content_image_upload_location(instance, filename):
    x = timezone.now()
    return "%s/%s/%s" %(x.year, x.month, x.day)

class ContentType(Enum):   # A subclass of Enum
    ARTICLE = "article"
    REPORT = "report"
    PROBLEM = "problem"
    COMMENT = "comment"

class Content(models.Model): # We want comment to have a foreign key to all contents so we use all of them as one
    title = models.CharField(max_length=255)
    type = models.CharField(
      max_length=30,
      choices=[(tag, tag.value) for tag in ContentType]  # Choices is a list of Tuple
    )
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to=content_image_upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    content = models.TextField()
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False)
    read_time = models.IntegerField(default=0)  # models.TimeField(null=True, blank=True) #assume minutes
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)


class ContentRealtionType(Enum):   # A subclass of Enum
    COMMENTED_ON = "commented_on"

class ContentRelation(models.Model):
    source = models.ForeignKey(Content, related_name='source', on_delete=models.CASCADE)
    destination = models.ForeignKey(Content, related_name='destination', on_delete=models.CASCADE)
    type = models.CharField(
      max_length=30,
      choices=[(tag, tag.value) for tag in ContentRealtionType]  # Choices is a list of Tuple
    )