from campaigns.api.serializers import ProductCreateSerializer, ProductListSerializer
from team.models import TeamUserRelation

from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import AllowAny


from campaigns.models import Product
from team.models import Team
class CreateProductAPIView(CreateAPIView):
  serializer_class = ProductCreateSerializer
  def perform_create(self, serializer):
      user = self.request.user
      product = serializer.save(seller = TeamUserRelation.objects.filter(user = user)[0].team)



class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]
    
    def get_queryset(self, *args, **kwargs):
        queryset_list = Product.objects.all()
        team_id = self.request.GET.get("group")
        if team_id:
            team = Team.objects.filter(id = team_id).first()
            queryset_list = queryset_list.filter(seller = team)
        return queryset_list
