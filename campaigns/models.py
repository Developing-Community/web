from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from companions.models import Application
from taxonomy.models import Term
from team.models import Team
from django.utils import timezone
from django.contrib.auth.models import User
from enumfields import EnumField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport

# Create your models here.


def campaign_image_upload_location(instance, filename):
    x = timezone.now()
    return "%s/%s/%s/%s" % (x.year, x.month, x.day, filename)


class CampaignType(Enum):
    WORK = "WORK"
    MENTORING = "MENTORING"
    STUDY = "STUDY"
    SALES = "SALES"


class Campaign(models.Model):  # We want comment to have a foreign key to all contents so we use all of them as one
    title = models.CharField(max_length=1000)

    # type = models.CharField(
    #     max_length=30,
    #     choices=[(tag.value, tag.name) for tag in CampaignType]
    # )

    type = EnumField(CampaignType, max_length=1)

    application = models.ForeignKey(Application, default=1, null=True, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=campaign_image_upload_location,
                              null=True,
                              blank=True,
                              width_field="width_field",
                              height_field="height_field")
    height_field = models.IntegerField(default=0)
    width_field = models.IntegerField(default=0)
    description = models.TextField()

    start_time = models.DateField(auto_now=False, auto_now_add=False)
    end_time = models.DateField(auto_now=False, auto_now_add=False)

    def __str__(self):
        return self.title


class CampaignPartyRelationType(Enum):  # A subclass of Enum
    CREATOR = "CREATOR"
    MANAGER = "MANAGER"
    MEMBER = "MEMBER"


class CampaignPartyRelation(models.Model):
    campaign = models.ForeignKey(Campaign, on_delete=models.CASCADE)

    # party
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    # type = models.CharField(
    #     max_length=30,
    #     choices=[(tag.value, tag.name) for tag in CampaignPartyRelationType]
    # )

    type = EnumField(CampaignPartyRelationType, max_length=1)

    def __str__(self):
        return str(self.content_object) + " | " + self.campaign.title



class CampaignTermRealtionType(Enum):
    SUBJECT = "SUBJECT"


class CampaignTermRelation(models.Model):
    campaign = models.ForeignKey(Campaign, related_name='campaign', on_delete=models.CASCADE)
    term = models.ForeignKey(Term, related_name='term', on_delete=models.CASCADE)

    # type = models.CharField(
    #     max_length=30,
    #     choices=[(tag.value, tag.name) for tag in CampaignTermRealtionType]
    # )

    type = EnumField(CampaignTermRealtionType, max_length=1)


# Sales Campaign

class Product(models.Model):
    seller = models.ForeignKey(Team, on_delete=models.CASCADE, blank=True, related_name="seller")
    name = models.CharField(blank=True, null=True, max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.IntegerField()
    profile_image = models.ImageField(null=True,
                                      blank=True,
                                      width_field="width_field",
                                      height_field="height_field")
    height_field = models.IntegerField(default=0, null=True)
    width_field = models.IntegerField(default=0, null=True)