from django.urls import path

from .views import TelegramTokenCreateAPIView, ProfileRetrieveAPIView

urlpatterns = [
    path('create-token/', TelegramTokenCreateAPIView.as_view(), name='create-token'),
    path('<int:telegram_user_id>/get-profile/', ProfileRetrieveAPIView.as_view(), name='get-profile'),
]
