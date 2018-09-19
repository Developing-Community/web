from enumfields import EnumField
from enumfields import Enum  # Uses Ethan Furman's "enum34" backport

from users.models import Profile
from django.db import models

from django.contrib.auth.models import User

class Team(models.Model):
    name = models.CharField(max_length=255)
    # user = models.ManyToManyField(Profile, on_delete=models.CASCADE, related_name="")

class TeamUserRelationType(Enum):  # A subclass of Enum
    CREATOR = "CREATOR"
    MANAGER = "MANAGER"
    MEMBER = "MEMBER"


class TeamUserRelation(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    type = EnumField(TeamUserRelationType, default=TeamUserRelationType.CREATOR, max_length=100)