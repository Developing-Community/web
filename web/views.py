from django.contrib import messages
from django.urls import reverse
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

from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from users.forms import UserRegisterForm
from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout,
)

from django.shortcuts import render, redirect

from web.forms import SharifSummerMarketProfileTempForm

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

    # # TODO: Bring register form here
    # form = UserRegisterForm(request.POST or None)
    # if form.is_valid():
    #     user = form.save(commit=False)
    #     password = form.cleaned_data.get('password')
    #     user.set_password(password)
    #     user.save()
    #     new_user = authenticate(username=user.username, password=password)
    #     login(request, new_user)
    #     return reverse('telegramgroups', kwargs={})
    #
    # context = {
    #     "form": form,
    # }

    context = {}
    return render(request, "learn-index.html", context)

def groups_view(request):
    return render(request, 'groups.html', {})




def sharif_summer_market_temp_view(request):
    form = SharifSummerMarketProfileTempForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, "فرم با موفقیت ثبت شد", extra_tags='html_safe')
    context = {
        "form": form,
    }

    return render(request, "landing.html", context)