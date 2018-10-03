from django.contrib.contenttypes.models import ContentType
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, UUIDField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import (
    ModelSerializer
)

from bot.models import TelegramToken
from users.models import Profile


class TelegramTokenSerializer(ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = [
            'verify_token',
            'telegram_user_id'
        ]


class BotProfileSerializer(ModelSerializer):
    link = HyperlinkedIdentityField(
        view_name='users:view-profile',
        lookup_field='id'
    )
    class Meta:
        model = Profile
        fields = [
            'id',
            'link',
            'telegram_user_id'
        ]