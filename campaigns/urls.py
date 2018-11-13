from django.urls import path

from campaigns.models import CampaignType
from content.models import ContentType
from .views import CreateProductAPIView, ProductListAPIView, CampaignListAPIView, CampaignCreateAPIView, \
    CampaignRequestEnrollmentAPIView, CampaignCancelRequestEnrollmentAPIView, CampaignDetailAPIView, \
    CampaignDeleteAPIView, CampaignUpdateAPIView, CampaignImageAPIView, CampaignContentCreateAPIView, \
    CampaignContentListAPIView

urlpatterns = [
    path('<int:pk>/', CampaignDetailAPIView.as_view(), name='detail'),
    path('<int:pk>/edit/', CampaignUpdateAPIView.as_view(), name='update'),
    path('<int:pk>/delete/', CampaignDeleteAPIView.as_view(), name='delete'),
    path('<int:pk>/request-enrollment/', CampaignRequestEnrollmentAPIView.as_view(), name='request-enrollment'),
    path('<int:pk>/cancel-request/', CampaignCancelRequestEnrollmentAPIView.as_view(), name='cancel-request'),
    path('<int:pk>/image/', CampaignImageAPIView.as_view()),

    path('<int:campaign_pk>/questions/', CampaignContentListAPIView.as_view(), {'type': ContentType.QUESTION},
         name='campaign-questions'),
    path('<int:campaign_pk>/partitions/', CampaignContentListAPIView.as_view(), {'type': ContentType.PARTITIONING},
         name='campaign-partitions'),

    path('<int:campaign_pk>/questions/create/', CampaignContentCreateAPIView.as_view(), {'type': ContentType.QUESTION},
         name='questions-create'),

    path('study/', CampaignListAPIView.as_view(), {'type': CampaignType.STUDY}, name='study-list'),
    path('mentoring/', CampaignListAPIView.as_view(), {'type': CampaignType.MENTORING}, name='mentoring-list'),
    path('study/create/', CampaignCreateAPIView.as_view(), {'type': CampaignType.STUDY}, name='create-study'),
    path('mentoring/create/', CampaignCreateAPIView.as_view(), {'type': CampaignType.MENTORING},
         name='create-mentoring'),
    path('product/create/', CreateProductAPIView.as_view(), name="create-product"),
    path('product/list/', ProductListAPIView.as_view(), name="create-product"),
]
