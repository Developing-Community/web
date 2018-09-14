from django.contrib.auth import get_user_model
from enumfields.drf import EnumField
from rest_framework.serializers import (
    ModelSerializer
)

from campaigns.models import Product, Campaign, CampaignType
from team.serializers import TeamListSerializer
from enumfields.drf.serializers import EnumSupportSerializerMixin
User = get_user_model()


class CampaignSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'type',
            'description',
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
