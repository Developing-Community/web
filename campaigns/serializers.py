from django.contrib.contenttypes.models import ContentType
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer
)

from campaigns.models import Product, Campaign, CampaignPartyRelation, CampaignPartyRelationType, \
    CampaignEnrollmentRequest
from team.serializers import TeamListSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


class CampaignCreateSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'start_time',
            'end_time',
            'description',
        ]


class CampaignListSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'start_time',
            'end_time',
            'description',
            'image',
            'width_field',
            'height_field',
        ]
    read_only_fields = [
      'image',
      'width_field',
      'height_field',
      ]

class CampaignUpdateSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'start_time',
            'end_time',
            'description',
        ]


class CampaignDetailSerializer(EnumSupportSerializerMixin, ModelSerializer):
    accessable = SerializerMethodField()
    requested = SerializerMethodField()
    enrolled = SerializerMethodField()
    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'type',
            'description',
            'start_time',
            'end_time',
            'accessable',
            'requested',
            'enrolled',
             'image',
             'width_field',
             'height_field',
        ]
    read_only_fields = [
      'image',
      'width_field',
      'height_field',
      ]

    def get_accessable(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and CampaignPartyRelation.objects.filter(
                campaign = obj,
                type = CampaignPartyRelationType.CREATOR,
                content_type = ContentType.objects.get(model="user"),
                object_id = user.id
        ).exists():
            return True
        return False

    def get_requested(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and CampaignEnrollmentRequest.objects.filter(
                campaign = obj,
                user = user
        ).exists():
            return True
        return False

    def get_enrolled(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and CampaignPartyRelation.objects.filter(
                campaign = obj,
                type = CampaignPartyRelationType.MEMBER,
                content_type = ContentType.objects.get(model="user"),
                object_id = user.id
        ).exists():
            return True
        return False


class CampaignImageUpdateRetriveSerializer(ModelSerializer):
  class Meta:
    model = Campaign
    fields = [
      'image',
      'width_field',
      'height_field',
    ]
    read_only_fields = [
      'width_field',
      'height_field',
      ]

class CampaignDeleteSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
        ]


class CampaignRequestEnrollmentSerializer(ModelSerializer):
  class Meta:
    model = CampaignEnrollmentRequest
    fields = [
        'note'
    ]

class ProductCreateSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
            'price'
        ]


class ProductListSerializer(ModelSerializer):
    seller = TeamListSerializer()

    class Meta:
        model = Product
        fields = [
            'seller',
            'id',
            'name',
            'description',
            'price'
        ]