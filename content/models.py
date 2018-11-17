from django.db import models
from django.utils import timezone
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
from enumfields import EnumField

from taxonomy.models import Term
from users.models import Profile
from web import settings


def content_image_upload_location(instance, filename):
    x = timezone.now()
    return "%s/%s/%s/%s" % (x.year, x.month, x.day, filename)


def content_attachment_upload_location(instance, filename):
    x = timezone.now()
    return "%s/%s/%s/%s" % (x.year, x.month, x.day, filename)


class ContentType(Enum):  # A subclass of Enum
    ARTICLE = "ARTICLE"
    ASSIGNMENT = "ASSIGNMENT"
    ANNOUNCEMENT = "ANNOUNCEMENT"
    REPORT = "REPORT"
    PROBLEM = "PROBLEM"
    SOLUTION = "SOLUTION"
    QUESTION = "QUESTION"
    ANSWER = "ANSWER"
    COMMENT = "COMMENT"
    STORY = "STORY"
    PROJECT = "PROJECT"
    EVENT = "EVENT"
    PARTITIONING = "PARTITIONING"  # parts of a book or tutorial being studied


class MainContentType(Enum):
    TEXT = "TEXT"
    VIDEO = "VIDEO"
    AUDIO = "AUDIO"
    FILE = "FILE"


class ContentVisibility(Enum):  # A subclass of Enum
    PUBLIC = "PUBLIC"
    PRIVATE = "PRIVATE"



class ContentRelationType(Enum):  # A subclass of Enum
    COMMENTED_ON = "COMMENTED_ON"
    ANSWERED_TO = "ANSWERED_TO"
    REPLIED_TO = "REPLIED_TO"

class Content(models.Model):  # We want comment to have a foreign key to all contents so we use all of them as one
    title = models.CharField(max_length=1000, blank=True, null=True)

    type = EnumField(ContentType, default=ContentType.ARTICLE, blank=True, max_length=1000)
    main_type = EnumField(MainContentType, default=MainContentType.TEXT, max_length=1000)

    # no api
    visibility = EnumField(ContentVisibility, default=ContentVisibility.PUBLIC, blank=True, max_length=1000)

    # no api
    # application = models.ForeignKey(Application, default=1, null=True, on_delete=models.CASCADE)

    # comes from logged in user
    author = models.ForeignKey(Profile, default=1, on_delete=models.CASCADE)

    # no api
    slug = models.SlugField(blank=True, null=True)

    # foriegn api
    # subject = models.ForeignKey(Term, related_name="subject", blank=True, null=True, on_delete=models.SET_NULL)
    image = models.ImageField(upload_to=content_image_upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    attachment = models.FileField(upload_to=content_attachment_upload_location,
                                  null=True,
                                  blank=True)

    # no api
    height_field = models.IntegerField(default=0)
    # no api
    width_field = models.IntegerField(default=0)
    content = models.TextField(null=True, blank=True)
    flash_note = models.TextField(blank=True, null=True)
    draft = models.BooleanField(default=False)
    publish = models.DateField(auto_now=False, auto_now_add=False, default=timezone.now, blank=True)
    # read_time = models.IntegerField(default=0)  # models.TimeField(null=True, blank=True) #assume minutes
    # no api
    updated = models.DateTimeField(auto_now=True, auto_now_add=False)
    # no api
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

    # TODO: Voting System
    # external api
    up_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="up_voters", blank=True)
    down_voters = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="down_voters", blank=True)

    @property
    def answers(self):
        return [rel.source for rel in ContentRelation.objects.filter(type=ContentRelationType.ANSWERED_TO, destination=self)]

    @property
    def comments(self):
        return [rel.source for rel in ContentRelation.objects.filter(type=ContentRelationType.COMMENTED_ON, destination=self)]

    @property
    def replies(self):
        return [rel.source for rel in ContentRelation.objects.filter(type=ContentRelationType.REPLIED_TO, destination=self)]

    def __str__(self):
        if self.title:
            return self.title
        else:
            return self.content[:20] + "..."

    class Meta:
        unique_together = ("slug", "type")


class ContentRelation(models.Model):
    source = models.ForeignKey(Content, related_name='source', on_delete=models.CASCADE)
    destination = models.ForeignKey(Content, related_name='destination', on_delete=models.CASCADE)
    type = EnumField(ContentRelationType, default=ContentRelationType.COMMENTED_ON, max_length=1000)

    def __str__(self):
        return str(self.source) + " | " + str(self.type) + " | " + str(self.destination)


class ContentTermRelationType(Enum):  # A subclass of Enum
    SKILLS_NEEDED = "SKILLS_NEEDED"


class ContentTermRelation(models.Model):
    content = models.ForeignKey(Content, related_name='contents', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, related_name='terms', on_delete=models.CASCADE)
    type = EnumField(ContentTermRelationType, max_length=1000)
