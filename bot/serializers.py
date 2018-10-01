from django.contrib.contenttypes.models import ContentType
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import (
    ModelSerializer
)

from bot.models import TelegramToken

class TelegramTokenSerializer(EnumSupportSerializerMixin, ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = [
            'user_token',
            'telegram_user_id'
        ]