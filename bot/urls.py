from django.urls import path

from .views import HandlePVAPIView

urlpatterns = [
    path('handle-pv/', HandlePVAPIView.as_view(), name='handle-pv'),
]
