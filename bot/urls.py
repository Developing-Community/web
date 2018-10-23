from django.urls import path

from .views import HandlePVAPIView, ProfileRetrieveAPIView

urlpatterns = [
    path('handle-pv/', HandlePVAPIView.as_view(), name='handle-pv'),
    path('<int:telegram_user_id>/get-profile/', ProfileRetrieveAPIView.as_view(), name='get-profile'),
]
