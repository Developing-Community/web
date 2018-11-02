from django.urls import path

from bot.views import TelegramTokenVerificationAPIView
from .views import (
    UserCreateAPIView,
    ProfileUpdateAPIView,
    UserProfileRetrieveAPIView,
    # profile-password-reset,
    reset_password_change, get_http_host,
    ProfileImageAPIView, ProfileRetrieveAPIView)

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
app_name = "users"
urlpatterns = [
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),
    path('auth/obtain_token/', obtain_jwt_token),
    path('auth/verify-telegram-token/', TelegramTokenVerificationAPIView.as_view(), name="verify-telegram-token"),
    path('profile/<int:pk>/profile-image/',ProfileImageAPIView.as_view()),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', UserProfileRetrieveAPIView.as_view(), name='view-user-profile'),
    path('profile/<int:id>/', ProfileRetrieveAPIView.as_view(), name='view-profile'),
    path('profile/<int:id>/update/', ProfileUpdateAPIView.as_view(), name='edit-profile'),
    path('reset-password/<key>/',reset_password_change,name="reset_password"),
    path('get-http-host/',get_http_host,name="get_http_host"),
]
