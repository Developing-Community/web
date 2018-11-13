from rest_framework.serializers import (
  ModelSerializer
)

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
