from rest_framework.generics import (
    CreateAPIView
)
from rest_framework.permissions import (
    AllowAny,
)
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from bot.models import TelegramToken
from .serializers import (
    TelegramTokenSerializer)

class TelegramTokenCreateAPIView(APIView):
    queryset = TelegramToken.objects.all()
    serializer_class = TelegramTokenSerializer
    permission_classes = [AllowAny]

    def post(self, request, format=None):
        telegram_user_id = request.data['telegram_user_id']
        x = TelegramToken.objects.filter(
            telegram_user_id = telegram_user_id)
        if x.exists():
            x = x.first()
        else:
            x = TelegramToken.objects.create(
            telegram_user_id = telegram_user_id)
        return Response(TelegramTokenSerializer(x).data)
