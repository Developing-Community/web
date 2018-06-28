"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token
from django.urls import path

from django.conf.urls.static import static
from web import views, settings
from .views import (
TelegramGroupsAPIView
    )

urlpatterns = [
    path('auth/refresh_token/', refresh_jwt_token),
    path('auth/verify_token/', verify_jwt_token),
    path('auth/obtain_token/', obtain_jwt_token),
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),

    path('api/user/', include('users.api.urls')),
    path('api/fields/', include('learningFields.api.urls')),

    path('', views.index_view, name='index'),
    path('groups/', views.groups_view, name='telegramgroups'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True), name='icon'),
    re_path(r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt', permanent=True), name='robots.txt'),
    path('trello/link',
         RedirectView.as_view(url='https://trello.com/invite/developingcommunity/0569c91ef09c6c05f437a75927640874',
                              permanent=True), name='trello'),
    path('slack/link', RedirectView.as_view(
        url='https://join.slack.com/t/developing-community/shared_invite/enQtMzc1ODU0NTA5MzAzLTE0NmI1MmY4ZGM5NjhiODY2MDFjNmFjYjg1OWExNTBjZmViMjRkMWE4Y2U1NDk1ZjdjYzM5ODhlZmYwZWQ0MTA',
        permanent=True), name='slack'),
    path('tgroups/', TelegramGroupsAPIView.as_view(), name='telegramgps'),
]