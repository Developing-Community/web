from django.contrib.contenttypes.models import ContentType
from enumfields.drf.serializers import EnumSupportSerializerMixin
from rest_framework.exceptions import ValidationError
from rest_framework.fields import SerializerMethodField, UUIDField
from rest_framework.serializers import (
    ModelSerializer
)

from bot.models import TelegramToken

class TelegramTokenSerializer(ModelSerializer):
    class Meta:
        model = TelegramToken
        fields = [
            'verify_token',
            'telegram_user_id'
        ]