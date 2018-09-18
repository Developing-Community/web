from django.urls import path

from .views import CreateProductAPIView, ProductListAPIView, CampaignListAPIView, CampaignCreateMentoringAPIView, \
    CampaignCreateStudyAPIView, CampaignDetailAPIView, CampaignDeleteAPIView, CampaignUpdateAPIView

urlpatterns = [
    path('', CampaignListAPIView.as_view(), name='list'),
    path('study/create/', CampaignCreateStudyAPIView.as_view(), name='create-study'),
    path('mentoring/create/', CampaignCreateMentoringAPIView.as_view(), name='create-mentoring'),
    path('<int:pk>/', CampaignDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', CampaignUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', CampaignDeleteAPIView.as_view(), name='delete'),

    path('product/create/', CreateProductAPIView.as_view(), name="create-product"),
    path('product/list/', ProductListAPIView.as_view(), name="create-product"),
]
