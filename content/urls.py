from django.urls import path,include
from rest_framework import routers

from .views import ContentViewSet

router = routers.DefaultRouter()
router.register("contents",ContentViewSet)

urlpatterns = [
    path('',include(router.urls)),
]