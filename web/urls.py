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
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.urls import path

from django.conf.urls.static import static

import content.views
import learning.views
import users.views
from web import views, settings
from .views import (
TelegramGroupsAPIView
    )



urlpatterns = [
    #APPs
    path('admin/', admin.site.urls),
    path('user/', include('users.urls')),
    path('profile/edit/', users.views.edit_profile , name='edit_profile'),

    #APP APIs
    path('api/user/', include('users.api.urls')),

    #general urls
    url(r'^$', views.index_view, name='index'),
    path('', include('users.api.urls')),

    path('mentoring/add/', learning.views.add_mentoring, name='add_mentoring'),

    path('articles/new/', content.views.add_article, name='add_article'),

    path('groups/', views.groups_view, name='telegramgroups'),
    path('trello/link',
         RedirectView.as_view(url='https://trello.com/invite/developingcommunity/0569c91ef09c6c05f437a75927640874',
                              permanent=True), name='trello'),
    path('slack/link', RedirectView.as_view(
        url=' ',
        permanent=True), name='slack'),
    re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True), name='icon'),
    re_path(r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt', permanent=True), name='robots.txt'),


    #general APIs
    path('tgroups/', TelegramGroupsAPIView.as_view(), name='telegramgps'),
]