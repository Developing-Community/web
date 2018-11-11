from django.db import models
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport
from enumfields import EnumField

from users.models import Profile
from web import settings


class Team(models.Model):
    name = models.CharField(max_length=255)
    # user = models.ManyToManyField(Profile, on_delete=models.CASCADE, related_name="")

    def __str__(self):
        return self.name

class TeamUserRelationType(Enum):  # A subclass of Enum
    CREATOR = "CREATOR"
    MANAGER = "MANAGER"
    MEMBER = "MEMBER"


class TeamUserRelation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    type = EnumField(TeamUserRelationType, default=TeamUserRelationType.CREATOR, max_length=1000)

    def __str__(self):
        return str(self.team) + " | " + str(self.profile)