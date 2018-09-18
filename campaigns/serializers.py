from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer
)

from campaigns.models import Product, Campaign, CampaignPartyRelation, CampaignPartyRelationType
from team.serializers import TeamListSerializer

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
            'enrolled',
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


class CampaignDeleteSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
        ]


class CampaignEnrollSerializer(ModelSerializer):
  class Meta:
    model = CampaignPartyRelation
    fields = [
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