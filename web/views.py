from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication
from django.contrib.auth.models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,

)

from django.shortcuts import render

from rest_framework_jwt.authentication import JSONWebTokenAuthentication


class TelegramGroupsAPIView(APIView):
    """
    View to list all users in the system.

    * Requires token authentication.
    * Only admin users are able to access this view.
    """
    authentication_class = (
        JSONWebTokenAuthentication,)  # Don't forget to add a 'comma' after first element to make it a tuple
    permission_classes = (IsAuthenticated,)

    def get(self, request, format=None):
        """
        Return a list of all users.
        """
        links = [
            {"لینک گروه برنامه نویسی": "https://t.me/joinchat/BzST0lBdHY9og6kPus_InQ"},
            {"لینک گروه هنر": "https://t.me/joinchat/BzST0lBqx8zMoRygUZyxvg"},
            {"لینک گروه علوم انسانی و پایه": "https://t.me/joinchat/BzST0ksuVjIOB2NUSZTUhg"},
        ]

        return Response(links)


def index_view(request):
    return render(request, 'index.html', {})


def groups_view(request):
    return render(request, 'groups.html', {})
