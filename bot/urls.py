from django.urls import path

from .views import HandlePVAPIView, HandleGPAPIView

urlpatterns = [
    path('handle-pv/', HandlePVAPIView.as_view(), name='handle-pv'),
    path('handle-gp/', HandleGPAPIView.as_view(), name='handle-gp'),
]
