from rest_framework.generics import CreateAPIView

from team.api.serializers import TeamCreateSerializer
from team.models import TeamUserRelation
class CreateTeamAPIView(CreateAPIView):
  serializer_class = TeamCreateSerializer

  

  def perform_create(self, serializer):
      team = serializer.save()
      user = self.request.user
      creator_relation = TeamUserRelation(
        team = team,
        user = user
      )
      creator_relation.save()