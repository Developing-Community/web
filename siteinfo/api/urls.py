from django.urls import path

from .views import (
TelegramGroupsAPIView
    )

urlpatterns = [
    # url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    path('tgroups/', TelegramGroupsAPIView.as_view(), name='register'),
]
