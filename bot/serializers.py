from django.contrib.contenttypes.models import ContentType
from django.urls import reverse
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, UUIDField
from rest_framework.relations import HyperlinkedIdentityField
from rest_framework.serializers import (
    ModelSerializer
)
from web.settings import HOST_URL
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
    link = SerializerMethodField()
    class Meta:
        model = Profile
        fields = [
            'id',
            'link',
            'telegram_user_id'
        ]
    def get_link(self, obj):
        return HOST_URL + reverse("users:view-profile", kwargs={'id':obj.id})