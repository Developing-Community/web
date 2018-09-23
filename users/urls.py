from django.urls import path

from .views import (
    UserCreateAPIView,
    ProfileUpdateAPIView,
    ProfileRetrieveAPIView,
    # profile-password-reset,
    reset_password_change,get_http_host,
    ProfileImageAPIView)

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
app_name = "user"
urlpatterns = [
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),
    path('auth/obtain_token/', obtain_jwt_token),
    path('profile/<int:pk>/profile-image/',ProfileImageAPIView.as_view()),
    path('register/', UserCreateAPIView.as_view(), name='register'),
    path('profile/', ProfileRetrieveAPIView.as_view(), name='view-profile'),
    path('profile/<int:id>/update/', ProfileUpdateAPIView.as_view(), name='edit-profile'),
    path('reset-password/<key>/',reset_password_change,name="reset_password"),
    path('get-http-host/',get_http_host,name="get_http_host"),
]
