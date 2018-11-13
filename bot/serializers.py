from django.urls import reverse
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer
)

from bot.models import TelegramProfile
from users.models import Profile
from web.settings import HOST_URL


class TelegramTokenSerializer(ModelSerializer):
    class Meta:
        model = TelegramProfile
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
        return HOST_URL + reverse("users:view-profile", kwargs={'id': obj.id})
