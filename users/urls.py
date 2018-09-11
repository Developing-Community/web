from django.urls import path

from .views import (
    UserCreateAPIView,
    )
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    # url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),
    path('auth/obtain_token/', obtain_jwt_token),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]
