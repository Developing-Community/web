from django.contrib.contenttypes.models import ContentType
from django.contrib.auth import get_user_model
from web.utils import RequiredValidator
from rest_framework.serializers import (
  CharField,
  EmailField,
  HyperlinkedIdentityField,
  ModelSerializer,
  SerializerMethodField,
  ValidationError
)

from users.models import Profile
from team.models import Team, TeamUserRelation

class TeamCreateSerializer(ModelSerializer):
  class Meta:
    model = Team
    fields = [
      'name'
    ]
    
class TeamListSerializer(ModelSerializer):
  class Meta:
    model = Team
    fields = [
      'id',
      'name'
    ]
    
class TeamEnrollSerializer(ModelSerializer):
  class Meta:
    model = TeamUserRelation
    fields = [
    ]