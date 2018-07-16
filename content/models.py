from enum import Enum
from django.db import models

from web import settings

#TODO: change upload location
def upload_location(instance, filename):
    #filebase, extension = filename.split(".")
    #return "%s/%s.%s" %(instance.id, instance.id, extension)
    PostModel = instance.__class__
    new_id = PostModel.objects.order_by("id").last().id + 1
    """
    instance.__class__ gets the model Post. We must use this method because the model is defined below.
    Then create a queryset ordered by the "id"s of each object,
    Then we get the last object in the queryset with `.last()`
    Which will give us the most recently created Model instance
    We add 1 to it, so we get what should be the same id as the the post we are creating.
    """
    return "%s/%s" %(new_id, filename)

class Hashtag(models.Model):
    title = models.CharField(max_length=255)


# TODO: complete Hashtag, Comment and Content
class Comment(models.Model):
    content = models.TextField()

class ContentType(Enum):   # A subclass of Enum
    ARTICLE = "article"
    REPORT = "report"
    PROBLEM = "problem"

class Content(models.Model): # We want comment to have a foreign key to all contents so we use all of them as one
    title = models.CharField(max_length=255)
    type = models.CharField(
      max_length=15,
      choices=[(tag, tag.value) for tag in ContentType]  # Choices is a list of Tuple
    )
    # #author = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    # slug = models.SlugField(unique=True)
    # image = models.ImageField(upload_to=upload_location,
    #                           null=True,
    #                           blank=True,
    #                           width_field="width_field",
    #                           height_field="height_field")
    # height_field = models.IntegerField(default=0)
    # width_field = models.IntegerField(default=0)
    # content = models.TextField()
    # draft = models.BooleanField(default=False)
    # publish = models.DateField(auto_now=False, auto_now_add=False)
    # read_time = models.IntegerField(default=0)  # models.TimeField(null=True, blank=True) #assume minutes
    # updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)
