from django.urls import path

from .views import (
    FieldListAPIView,
    )

urlpatterns = [
    path('', FieldListAPIView.as_view(), name='list'),
]
