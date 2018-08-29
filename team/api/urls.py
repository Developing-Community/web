from django.urls import path

from team.api.views import CreateTeamAPIView
urlpatterns = [
    path('create/', CreateTeamAPIView.as_view(), name="create-team"),
]
