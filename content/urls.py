from django.urls import path,include
from rest_framework import routers

from .views import ContentListView,ContentCreateView,ContentUpdateView,ContentDelete


urlpatterns = [
    path('<int:pk>/',ContentUpdateView),
    path('list/',ContentListView.as_view()),
    path('create/',ContentCreateView.as_view()),
    path('<int:pk>/delete/',ContentDelete),
]