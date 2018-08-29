from rest_framework.generics import CreateAPIView

from campaigns.api.serializers import ProductCreateSerializer
from team.models import TeamUserRelation
class CreateProductAPIView(CreateAPIView):
  serializer_class = ProductCreateSerializer

  

  def perform_create(self, serializer):
      user = self.request.user
      product = serializer.save(seller = TeamUserRelation.objects.filter(user = user)[0].team)