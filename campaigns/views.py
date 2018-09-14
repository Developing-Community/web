from django.db.models import Q


from rest_framework.filters import (
        SearchFilter,
        OrderingFilter,
    )
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
    )



from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

    )

from team.models import Team, TeamUserRelation
from campaigns.models import Campaign, CampaignPartyRelation, CampaignPartyRelationType, Product

from .pagination import CampaignLimitOffsetPagination, CampaignPageNumberPagination
from .permissions import IsOwnerOrReadOnly

from .serializers import (
    CampaignSerializer,
    ProductListSerializer, ProductCreateSerializer)


class CampaignCreateAPIView(CreateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        campaign = serializer.save()
        user = self.request.user

        creator_relation = CampaignPartyRelation(
            campaign=campaign,
            content_object=user,
            type=CampaignPartyRelationType.CREATOR
        )
        creator_relation.save()


class CampaignDetailAPIView(RetrieveAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    lookup_field = 'id'
    permission_classes = [AllowAny]


class CampaignUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly]
    def perform_update(self, serializer):
        serializer.save(user=self.request.user)



class CampaignDeleteAPIView(DestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer
    lookup_field = 'id'
    permission_classes = [IsOwnerOrReadOnly]
    #lookup_url_kwarg = "abc"


class CampaignListAPIView(ListAPIView):
    serializer_class = CampaignSerializer
    filter_backends= [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = [
        'title',
        'type'
    ]
    pagination_class = CampaignPageNumberPagination #PageNumberPagination

    def get_queryset(self, *args, **kwargs):
        #queryset_list = super(CampaignListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Campaign.objects.all() #filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                    Q(title__icontains=query)|
                    Q(type__icontains=query)
                    ).distinct()
        return queryset_list

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
