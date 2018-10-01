from django.urls import path

from .views import TelegramTokenCreateAPIView
urlpatterns = [
    path('create-token/', TelegramTokenCreateAPIView.as_view(), name='create-token'),
]
