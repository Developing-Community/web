from django.contrib.auth import get_user_model
from django.contrib.contenttypes.models import ContentType
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer
)
from sorl_thumbnail_serializer.fields import HyperlinkedSorlImageField

from campaigns.models import Product, Campaign, CampaignPartyRelation, CampaignPartyRelationType, \
    CampaignEnrollmentRequest
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
    creator = SerializerMethodField()

    # A thumbnail image, sorl options and read-only
    thumbnail = HyperlinkedSorlImageField(
        '500x500',
        options={"crop": "center"},
        source='image',
        read_only=True
    )


    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'creator',
            'start_time',
            'end_time',
            'description',
            'thumbnail',
            'image',
            'width_field',
            'height_field',
        ]

    read_only_fields = [
        'thumbnail',
        'image',
        'width_field',
        'height_field',
    ]

    def get_creator(self, obj):
        return CampaignPartyRelation.objects.get(
            campaign=obj,
            type=CampaignPartyRelationType.CREATOR,
        ).content_object.name


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
    creator = SerializerMethodField()
    requested = SerializerMethodField()
    enrolled = SerializerMethodField()
    # A thumbnail image, sorl options and read-only
    thumbnail = HyperlinkedSorlImageField(
        '500x500',
        options={"crop": "center"},
        source='profile_image',
        read_only=True
    )

    # A larger version of the image, allows writing
    # profile_image = HyperlinkedSorlImageField('1024')

    class Meta:
        model = Campaign
        fields = [
            'id',
            'title',
            'creator',
            'type',
            'description',
            'start_time',
            'end_time',
            'accessable',
            'requested',
            'enrolled',
            'thumbnail',
            'image',
            'width_field',
            'height_field',
        ]

    read_only_fields = [
            'thumbnail',
        'image',
        'width_field',
        'height_field',
    ]

    def get_accessable(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and CampaignPartyRelation.objects.filter(
                campaign=obj,
                type=CampaignPartyRelationType.CREATOR,
                content_type=ContentType.objects.get(model="profile"),
                object_id=user.id
        ).exists():
            return True
        return False

    def get_creator(self, obj):
        return CampaignPartyRelation.objects.get(
            campaign=obj,
            type=CampaignPartyRelationType.CREATOR,
        ).content_object.name

    def get_requested(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and CampaignEnrollmentRequest.objects.filter(
                campaign=obj,
                user=user
        ).exists():
            return True
        return False

    def get_enrolled(self, obj):
        user = self.context.get('request').user
        if user.is_authenticated and CampaignPartyRelation.objects.filter(
                campaign=obj,
                type=CampaignPartyRelationType.MEMBER,
                content_type=ContentType.objects.get(model="user"),
                object_id=user.id
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
