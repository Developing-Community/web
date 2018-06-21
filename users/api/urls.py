from django.urls import path

from .views import (
    UserCreateAPIView,
    # UserLoginAPIView
    )

urlpatterns = [
    # url(r'^login/$', UserLoginAPIView.as_view(), name='login'),
    path('register/', UserCreateAPIView.as_view(), name='register'),
]
