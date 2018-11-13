from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from django.db.models import Q
from django.http import Http404
from rest_framework import status
from rest_framework.exceptions import ValidationError, ParseError
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
from rest_framework.parsers import MultiPartParser
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework.views import APIView

from campaigns.models import Campaign, CampaignPartyRelation, CampaignPartyRelationType, Product, \
    CampaignEnrollmentRequest, CampaignContentRelation
from content.models import Content
from content.serializers import ContentCreateSerializer, ContentSerializer
from taxonomy.models import Term
from team.models import Team, TeamUserRelation
from .pagination import CampaignPageNumberPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import (
    CampaignCreateSerializer,
    CampaignListSerializer,
    CampaignDetailSerializer,
    CampaignDeleteSerializer,
    CampaignUpdateSerializer,
    ProductListSerializer, ProductCreateSerializer, CampaignRequestEnrollmentSerializer,
    CampaignImageUpdateRetriveSerializer)

User = get_user_model()


class CampaignCreateAPIView(CreateAPIView):
    serializer_class = CampaignCreateSerializer

    def perform_create(self, serializer):
        campaign = serializer.save(type=self.kwargs['type'])
        user = self.request.user

        creator_relation = CampaignPartyRelation(
            campaign=campaign,
            content_object=user.profile,
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


class CampaignRequestEnrollmentAPIView(CreateAPIView):
    serializer_class = CampaignRequestEnrollmentSerializer

    def perform_create(self, serializer):
        user = self.request.user

        try:
            obj = Campaign.objects.get(pk=self.kwargs['pk'])
        except Campaign.DoesNotExist:
            raise Http404
        if (CampaignPartyRelation.objects.filter(
                campaign=obj,
                content_type=ContentType.objects.get(model="profile"),
                object_id=user.profile.first().id
        ).exists()):
            raise ValidationError("Already a member")
        if (CampaignEnrollmentRequest.objects.filter(
                campaign=Campaign.objects.get(pk=self.kwargs['pk']),
                user=user,
        ).exists()):
            raise ValidationError("Already requested")
        serializer.save(
            campaign=Campaign.objects.get(pk=self.kwargs['pk']),
            user=user,
        )


class CampaignCancelRequestEnrollmentAPIView(APIView):
    def post(self, request, pk):
        CampaignEnrollmentRequest.objects.filter(
            campaign=Campaign.objects.get(pk=pk),
            user=request.user,
        ).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


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


class CampaignImageAPIView(APIView):
    queryset = Campaign.objects.all()
    serializer_class = CampaignImageUpdateRetriveSerializer
    parser_classes = [MultiPartParser]

    def get(self, request, pk, format=None):
        campaign = Campaign.objects.filter(pk=pk).first()
        return Response(CampaignImageUpdateRetriveSerializer(campaign).data)

    def put(self, request, pk, format=None):
        campaign = Campaign.objects.filter(pk=pk).first()
        campaign.profile_image = request.data['profile_image']
        campaign.save()
        return Response(CampaignImageUpdateRetriveSerializer(campaign).data)

    def delete(self, request, pk, format=None):
        campaign = Campaign.objects.filter(pk=pk).first()
        campaign.image = None
        campaign.save()
        return Response({"status": "Campaign Image Removed"})


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


class CampaignContentCreateAPIView(CreateAPIView):
    serializer_class = ContentCreateSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):
        current_user = User.objects.all().first()  # self.request.user
        subject_str = serializer.validated_data['subject']
        campaign = Campaign.objects.filter(pk=self.kwargs['campaign_pk'])
        if campaign.exists():
            campaign = campaign.first()
        else:
            raise ParseError("Campaign not found")
        # get subject
        try:
            subject = Term.objects.get(title=subject_str)
        except Term.DoesNotExist:
            subject = Term(title=subject_str)
            subject.save()
        content = serializer.save(author=current_user, subject=subject, type=self.kwargs['type'])
        CampaignContentRelation.objects.create(content=content, campaign=campaign)


class CampaignContentListAPIView(ListAPIView):
    serializer_class = ContentSerializer
    filter_backends = [SearchFilter, OrderingFilter]
    permission_classes = [AllowAny]
    search_fields = [
        'title',
        'type'
    ]

    pagination_class = CampaignPageNumberPagination  # PageNumberPagination
    ordering = ['-id']

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        # user = self.request.user
        campaign = Campaign.objects.filter(pk=self.kwargs['campaign_pk'])
        if not campaign.exists():
            raise ParseError("Campaign doesn't exist")
        campaign = campaign.first()
        list_of_ids = [content.id for content in Content.objects.all() if
                       CampaignContentRelation.objects.filter(campaign=campaign,
                                                              content=content).exists() and content.type == self.kwargs[
                           'type']]
        return Content.objects.filter(pk__in=list_of_ids)
