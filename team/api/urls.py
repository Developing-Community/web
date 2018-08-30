from django.urls import path

from team.api.views import TeamCreateAPIView, TeamListAPIView, TeamEnrollAPIView
urlpatterns = [
    path('list/', TeamListAPIView.as_view(), name="list-teams"),
    path('create/', TeamCreateAPIView.as_view(), name="create-team"),
    path('enroll/', TeamEnrollAPIView.as_view(), name="create-team"),
]
