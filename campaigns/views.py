from django.db.models import Q
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)
from rest_framework.generics import (
    CreateAPIView,
    DestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
    RetrieveUpdateAPIView
)
from rest_framework.permissions import (
    AllowAny,
)
from django.http import Http404
from django.contrib.contenttypes.models import ContentType
from campaigns.models import Campaign, CampaignPartyRelation, CampaignPartyRelationType, Product, CampaignType
from team.models import Team, TeamUserRelation
from .pagination import CampaignPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CampaignCreateSerializer,
    CampaignListSerializer,
    CampaignDetailSerializer,
    CampaignDeleteSerializer,
    CampaignUpdateSerializer,
    ProductListSerializer, ProductCreateSerializer, CampaignEnrollSerializer)


class CampaignCreateAPIView(CreateAPIView):
    serializer_class = CampaignCreateSerializer

    def perform_create(self, serializer):
        campaign = serializer.save(type=self.kwargs['type'])
        user = self.request.user

        creator_relation = CampaignPartyRelation(
            campaign=campaign,
            content_object=user,
            type=CampaignPartyRelationType.CREATOR
        )
        creator_relation.save()


class CampaignDetailAPIView(RetrieveAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignDetailSerializer
    permission_classes = [AllowAny]


class CampaignUpdateAPIView(RetrieveUpdateAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignUpdateSerializer
    permission_classes = [IsOwnerOrReadOnly]

    def perform_update(self, serializer):
        serializer.save(user=self.request.user)


class CampaignDeleteAPIView(DestroyAPIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignDeleteSerializer
    permission_classes = [IsOwnerOrReadOnly]

class CampaignEnrollAPIView(CreateAPIView):
  serializer_class = CampaignEnrollSerializer
  permission_classes = [AllowAny]
  def perform_create(self, serializer):
      user = self.request.user

      try:
          obj = Campaign.objects.get(pk=self.kwargs['pk'])
      except Campaign.DoesNotExist:
          raise Http404


      print(user.is_authenticated and CampaignPartyRelation.objects.filter(
              campaign=obj,
              type=CampaignPartyRelationType.MEMBER,
              content_type=ContentType.objects.get(model="user"),
              object_id=user.id
      ).exists())
          # serializer.save(
          #   campaign = Campaign.objects.get(pk=self.request.query_params.pk),
          #   content_object = user,
          #   type = CampaignPartyRelationType.MEMBER
          # )

class CampaignListAPIView(ListAPIView):
    serializer_class = CampaignListSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = [
        'title',
        'type'
    ]

    pagination_class = CampaignPageNumberPagination  # PageNumberPagination
    ordering = ['-id']
    def get_queryset(self, *args, **kwargs):
        # queryset_list = super(CampaignListAPIView, self).get_queryset(*args, **kwargs)
        queryset_list = Campaign.objects.filter(type=self.kwargs['type'])  # filter(user=self.request.user)
        query = self.request.GET.get("q")
        if query:
            queryset_list = queryset_list.filter(
                Q(title__icontains=query) |
                Q(type__icontains=query)
            ).distinct()
        return queryset_list



class CreateProductAPIView(CreateAPIView):
    serializer_class = ProductCreateSerializer

    def perform_create(self, serializer):
        user = self.request.user
        product = serializer.save(seller=TeamUserRelation.objects.filter(user=user)[0].team)


class ProductListAPIView(ListAPIView):
    serializer_class = ProductListSerializer
    permission_classes = [AllowAny]

    def get_queryset(self, *args, **kwargs):
        queryset_list = Product.objects.all()
        team_id = self.request.GET.get("group")
        if team_id:
            team = Team.objects.filter(id=team_id).first()
            queryset_list = queryset_list.filter(seller=team)
        return queryset_list
