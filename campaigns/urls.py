from django.urls import path

from .views import CreateProductAPIView, ProductListAPIView, CampaignListAPIView, CampaignCreateAPIView, \
    CampaignDetailAPIView, CampaignDeleteAPIView, CampaignUpdateAPIView

urlpatterns = [
    path('', CampaignListAPIView.as_view(), name='list'),
    path('create/', CampaignCreateAPIView.as_view(), name='create'),
    path('<int:id>/', CampaignDetailAPIView.as_view(), name='detail'),
    path('<int:id>/edit/', CampaignUpdateAPIView.as_view(), name='update'),
    path('<int:id>/delete/', CampaignDeleteAPIView.as_view(), name='delete'),

    path('product/create/', CreateProductAPIView.as_view(), name="create-product"),
    path('product/list/', ProductListAPIView.as_view(), name="create-product"),
]