from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from team.api.serializers import TeamCreateSerializer, TeamListSerializer, TeamEnrollSerializer
from team.models import Team, TeamUserRelation, TeamUserRelationType

class TeamCreateAPIView(CreateAPIView):
  serializer_class = TeamCreateSerializer
  def perform_create(self, serializer):
      team = serializer.save()
      user = self.request.user
      creator_relation = TeamUserRelation(
        team = team,
        user = user,
        type = TeamUserRelationType.CREATOR
      )
      creator_relation.save()
      print(creator_relation.type)


class TeamEnrollAPIView(CreateAPIView):
  serializer_class = TeamEnrollSerializer
  permission_classes = [AllowAny]
  def perform_create(self, serializer):
      user = self.request.user
      serializer.save(
        team = Team.objects.filter(id=self.request.data['group'])[0],
        user = user,
        type = TeamUserRelationType.MANAGER
      )


class TeamListAPIView(ListAPIView):
    serializer_class = TeamListSerializer
    permission_classes = [AllowAny]
    queryset = Team.objects.all()
