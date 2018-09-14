from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny
from .serializers import TeamCreateSerializer, TeamListSerializer, TeamEnrollSerializer
from .models import Team, TeamUserRelation, TeamUserRelationType

class TeamCreateAPIView(CreateAPIView):
  serializer_class = TeamCreateSerializer
  def perform_create(self, serializer):
      team = serializer.save()
      user = self.request.user

      #TODO: IMPORTANT! remove after sharif market finished
      TeamUserRelation.objects.filter(user = user).delete()
      
      creator_relation = TeamUserRelation(
        team = team,
        user = user,
        type = "CREATOR"
      )
      creator_relation.save()
      print(creator_relation.type)


class TeamEnrollAPIView(CreateAPIView):
  serializer_class = TeamEnrollSerializer
  permission_classes = [AllowAny]
  def perform_create(self, serializer):
      user = self.request.user

      #TODO: IMPORTANT! remove after sharif market finished
      TeamUserRelation.objects.filter(user = user).delete()

      serializer.save(
        team = Team.objects.filter(id=self.request.data['group'])[0],
        user = user,
        type = TeamUserRelationType.MANAGER
      )


class TeamListAPIView(ListAPIView):
    serializer_class = TeamListSerializer
    permission_classes = [AllowAny]
    queryset = Team.objects.all()

class GetUserTeamAPIView(ListAPIView):
    serializer_class = TeamListSerializer
    def get_queryset(self, *args, **kwargs):
        return [x.team for x in TeamUserRelation.objects.filter(user = self.request.user)]