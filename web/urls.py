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
from django.urls import include, re_path
from django.urls import path
from django.views.generic import RedirectView, TemplateView

from django.conf.urls.static import static
import content.views
import learning.views
import users.views

from django_rest_passwordreset import urls as password_reset_urls
from web import views, settings

urlpatterns = [
  path('admin/', admin.site.urls),
  path('api/user/', include('users.urls')),
  path('api/bot/', include('bot.urls')),
  path('api/team/', include('team.urls')),
  path('api/campaigns/', include('campaigns.urls')),
  path('api/content/',include('content.urls'),name="content_api"),
  path('api/reset-password/',include(password_reset_urls,namespace="web")),
  # path('campaigns/sharifmarket/', views.sharif_summer_market_temp_view, name='sharif_summer_market_temp_view'),
  # path('user/', include('users.urls')),
  # path('profile/edit/', users.views.edit_profile , name='edit_profile'),
  #
  # #APP APIs
  #
  # #general urls
  # url(r'^$', RedirectView.as_view(url='/learn/', permanent=True), name='index'),
  # url('learn/', views.index_view, name='learn'),
  #
  # path('', include('users.api.urls')),
  #
  # path('campaigns/sharifmarket/', views.sharif_summer_market_temp_view, name='sharif_summer_market_temp_view'),
  #
  # path('mentoring/add/', learning.views.add_mentoring, name='add_mentoring'),
  #
  # path('articles/new/', content.views.add_article, name='add_article'),
  # path('reports/new/', content.views.add_report, name='add_report'),
  #
  # path('groups/', views.groups_view, name='telegramgroups'),
  # path('trello/link',
  #      RedirectView.as_view(url='https://trello.com/invite/developingcommunity/0569c91ef09c6c05f437a75927640874',
  #                           permanent=True), name='trello'),
  # path('slack/link', RedirectView.as_view(
  #     url=' ',
  #     permanent=True), name='slack'),
  # re_path(r'^favicon\.ico$', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True), name='icon'),
  # re_path(r'^robots\.txt$', RedirectView.as_view(url='/static/robots.txt', permanent=True), name='robots.txt'),
  #
  #
  # #general APIs
  # path('tgroups/', views.TelegramGroupsAPIView.as_view(), name='telegramgps'),
  #
  #
  #
  #
  #   url(r'^$', TemplateView.as_view(template_name="index.html")),
  #   url(r'^.*/$', TemplateView.as_view(template_name="index.html")),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)