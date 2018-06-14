from django.conf.urls import url
from django.contrib import admin

from .views import (
    FieldListAPIView,
    )

urlpatterns = [
    url('', FieldListAPIView.as_view(), name='list'),
]
