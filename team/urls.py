from django.urls import path

from .views import TeamCreateAPIView, TeamListAPIView, TeamEnrollAPIView, GetUserTeamAPIView
urlpatterns = [
    path('list/', TeamListAPIView.as_view(), name="list-teams"),
    path('create/', TeamCreateAPIView.as_view(), name="create-team"),
    path('enroll/', TeamEnrollAPIView.as_view(), name="enroll-team"),
    path('getuserteam/', GetUserTeamAPIView.as_view(), name="get-user-team"),
]
